# fastapi imports
from fastapi import APIRouter
from fastapi import Depends

# sqlalchemy imports
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

# project imports
from database.models import User
from schemas.user import UserCreate, UserResponce
from database.base import get_db_session

# other 
from authx import AuthX, AuthXConfig



config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "my_acces_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)

user_router = APIRouter(prefix='/users', tags=['users'])

@user_router.post("/login",response_model=UserResponce)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db_session),

):
