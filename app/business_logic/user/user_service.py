# import hashlib

# from fastapi import HTTPException

# from data_access.users.users_repository import UsersRepository
# from data_access.db.models import User
# from api.users.users_schemas import LoginUser, UserCreate, UserDelete, RegisterUser


# class UsersService:
#     def __init__(self, repo: UsersRepository):
#         self.repo = repo

#     async def get_users(self):
#         return await self.repo.get_all()

#     async def get_user_by_id(self, user_id: int):
#         user = await self.repo.get_by_id(user_id)
#         if not user:
#             raise ValueError("User not found")
#         return user

#     async def get_user_by_email(self, email: str):
#         user = await self.repo.get_by_email(email)
#         if not user:
#             raise ValueError("User not found")
#         return user

#     async def create_user(self, data: UserCreate):
#         # здесь может быть любая бизнес-логика
#         # проверки, логирование, интеграции и т.п.

#         user = User(
#             name=data.name,
#             email=data.email
#         )
#         return await self.repo.create(user)
    
#     async def delete_user(self, data: UserDelete):
#         user = User(
#             id = data.id
#         )
#         return await self.repo.delete(user)
    
    
    
#     async def register_user(self, data: RegisterUser):
#         print("TTTTTTTT")
#         db_user = self.get_user_by_email(email=data.email)
#         if db_user:
#             raise HTTPException(status_code=400)
#         else:
#             hash_password = hashlib.sha224(user.password.encode()).hexdigest()

#         user = User(
#             id = data.id,
#             first_name = data.first_name,
#             last_name = data.last_name,
#             phone = data.phone,
#             email = data.email,
#             role_id = data.role_id,
#             password_hash = hash_password,
#         )

#         user_db = await self.repo.create(user)
#         print("RRRR ", user_db)

from fastapi import HTTPException, status

from data_access.users.users_repository import UsersRepository
from data_access.db.models import User
from api.users.users_schemas import LoginUser, UserCreate, UserDelete, RegisterUser
from business_logic.user.security import hash_password, verify_password, create_access_token


class UsersService:
    def __init__(self, repo: UsersRepository):
        self.repo = repo

    async def get_users(self):
        return await self.repo.get_all()

    async def get_user_by_id(self, user_id: int):
        user = await self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user

    async def get_user_by_email(self, email: str):
        return await self.repo.get_by_email(email)

    async def create_user(self, data: UserCreate):
        user = User(
            name=data.name,
            email=data.email
        )
        return await self.repo.create(user)

    async def delete_user(self, data: UserDelete):
        user = User(id=data.id)
        return await self.repo.delete(user)

    async def register_user(self, data: RegisterUser):
        db_user = await self.get_user_by_email(email=data.email)

        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this email already exists"
            )

        user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            phone=data.phone,
            email=data.email,
            role_id=data.role_id,
            password_hash=hash_password(data.password_hash),
        )

        user_db = await self.repo.create(user)

        access_token = create_access_token(
            user_id=user_db.id,
            email=user_db.email
        )

        return {
            "message": "User registered successfully",
            "access_token": access_token,
            "token_type": "bearer",
            "user": user_db
        }

    async def login_user(self, data: LoginUser):
        db_user = await self.get_user_by_email(email=data.email)

        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        if not verify_password(data.password_hash, db_user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        access_token = create_access_token(
            user_id=db_user.id,
            email=db_user.email
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    