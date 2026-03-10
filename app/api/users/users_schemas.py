import re

from pydantic import BaseModel, EmailStr, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class UserCreate(BaseModel):
    name: str
    email: EmailStr


class UserRead(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True  # для SQLAlchemy моделей

class UserDelete(BaseModel):
    id: int
    
    class Config:
        from_attributes = True

class RegisterUser(BaseModel):
    id: int
    last_name: str
    first_name: str
    phone: str
    email: EmailStr
    role_id: int=2
    password_hash: str = Field(
        min_length=8,
        max_length=64,
        description="Password must be 8-64 characters"
    )
    
    @field_validator("password_hash")
    @classmethod
    def validate_password_strength(cls, value: str) -> str:
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        return value
    
    class Config:
        from_attributes = True

class LoginUser(BaseModel):
    id: int
    email: EmailStr
    role_id: int=2
    password_hash: str = Field(
        min_length=8,
        max_length=64,
        description="Password must be 8-64 characters"
    )
    
    @field_validator("password_hash")
    @classmethod
    def validate_password_strength(cls, value: str) -> str:
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")
        return value
    
    class Config:
        from_attributes = True
