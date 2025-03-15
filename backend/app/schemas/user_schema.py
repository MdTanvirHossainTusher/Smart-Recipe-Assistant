from typing import Optional
from pydantic import BaseModel, Field, EmailStr, model_validator


class UserBase(BaseModel):
    username: str = Field(..., description="Username")
    email: EmailStr = Field(..., description="Email address")
    password: str = Field(..., min_length=8, description="Password (minimum 8 characters)")



class UserCreateRequest(UserBase):
    @model_validator(mode='after')
    def validate_fields(self):
        if self.username.strip() == "":
            raise ValueError("Username can't be empty")

        password = self.password
        if not any(char.isupper() for char in password):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in password):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one digit')
        if not any(not char.isalnum() for char in password):
            raise ValueError('Password must contain at least one special character')

        return self


class UserUpdateRequest(BaseModel):
    password: Optional[str] = Field(None, min_length=8, description="New password (minimum 8 characters)")

    @model_validator(mode='after')
    def validate_password(self):
        if self.password is not None:
            password = self.password
            if password.strip() == "":
                raise ValueError("Password can't be empty")
            if not any(char.isupper() for char in password):
                raise ValueError('Password must contain at least one uppercase letter')
            if not any(char.islower() for char in password):
                raise ValueError('Password must contain at least one lowercase letter')
            if not any(char.isdigit() for char in password):
                raise ValueError('Password must contain at least one digit')
            if not any(not char.isalnum() for char in password):
                raise ValueError('Password must contain at least one special character')
        return self


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True