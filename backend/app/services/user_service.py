import logging

from passlib.context import CryptContext
from sqlalchemy.orm import Session

from backend.app.exceptions.custom_exception import DatabaseException, ResourceNotFoundException
from backend.app.models import Profile
from backend.app.models.User import User
from backend.app.schemas.user_schema import UserCreateRequest, UserUpdateRequest, UserResponse

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    def _get_user_or_404(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise ResourceNotFoundException(f"User with ID: {user_id} does not exist")
        return user

    def get_all_users(self):
        try:
            return self.db.query(User).all()
        except Exception as e:
            logger.error(f"Error fetching users: {str(e)}")
            raise DatabaseException(f"Error fetching users: {str(e)}")

    def get_user_by_id(self, user_id: int):
        try:
            user = self._get_user_or_404(user_id)
            return UserResponse(**user.__dict__)
        except ResourceNotFoundException:
            raise
        except Exception as e:
            logger.error(f"Error retrieving user: {str(e)}")
            raise DatabaseException(f"Error retrieving user: {str(e)}")

    def create_user(self, user: UserCreateRequest):
        try:
            new_user = User()
            if user.username is not None: new_user.username = user.username
            if user.email is not None: new_user.email = str(user.email)
            if user.password is not None: new_user.password = self.bcrypt_context.hash(user.password)

            # new_user.profile = Profile(user=new_user)
            new_user.profile = Profile(user=new_user)
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)

            # new_profile = Profile(user_id=new_user.id)  # Use user_id instead of new_user object
            # self.db.add(new_profile)
            # self.db.commit()
            # self.db.refresh(new_profile)

            return UserResponse(**new_user.__dict__)
        except Exception as e:
            logger.error(f"Error creating user: {str(e)}")
            raise DatabaseException(f"Error creating user: {str(e)}")

    def update_user(self, user_id: int, updated_user: UserUpdateRequest):
        try:
            user = self._get_user_or_404(user_id)
            if updated_user.password is not None:
                user.password = self.bcrypt_context.hash(updated_user.password)

            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)

            return UserResponse(**user.__dict__)
        except ResourceNotFoundException:
            raise
        except Exception as e:
            logger.error(f"Error updating user: {str(e)}")
            raise DatabaseException(f"Error updating user: {str(e)}")

    def delete_user(self, user_id: int):
        try:
            user = self._get_user_or_404(user_id)
            self.db.delete(user)
            self.db.commit()
            return {"message": "User deleted successfully"}
        except ResourceNotFoundException:
            raise
        except Exception as e:
            logger.error(f"Error deleting user: {str(e)}")
            raise DatabaseException(f"Error deleting user: {str(e)}")