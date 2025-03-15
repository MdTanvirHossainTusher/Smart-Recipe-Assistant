from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from backend.app.database import get_db
from backend.app.schemas.user_schema import UserResponse, UserCreateRequest, UserUpdateRequest
from backend.app.services.user_service import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.get("", response_model=list[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    return UserService(db).get_all_users()


@router.get("/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).get_user_by_id(user_id)


@router.post("")
async def create_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    return UserService(db).create_user(user)


@router.put("/{user_id}")
async def update_user(user_id: int, updated_user: UserUpdateRequest, db: Session = Depends(get_db)):
    return UserService(db).update_user(user_id, updated_user)


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService(db).delete_user(user_id)
