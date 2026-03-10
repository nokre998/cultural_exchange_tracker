from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.users_schemas import LoginUser, UserCreate, UserDelete, UserRead, RegisterUser
from data_access.db.session import get_db
from data_access.users.users_repository import UsersRepository
from business_logic.user.user_service import UsersService
from fastapi import status

router = APIRouter()


def get_users_service(db: AsyncSession = Depends(get_db)) -> UsersService:
    repo = UsersRepository(db)
    return UsersService(repo)


@router.get("/", response_model=list[UserRead])
async def get_users(
    service: UsersService = Depends(get_users_service),
):
    return await service.get_users()


@router.post("/", response_model=UserRead)
async def create_user(
    user: UserCreate,
    service: UsersService = Depends(get_users_service),
):
    try:
        return await service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: UserDelete,
    service: UsersService = Depends(get_users_service),
):
    try:
        return await service.delete_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    user: RegisterUser,
    service: UsersService = Depends(get_users_service),
):
    try:
        return await service.register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login_user(
    user: LoginUser,
    service: UsersService = Depends(get_users_service),
):
    try:
        return await service.register_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))