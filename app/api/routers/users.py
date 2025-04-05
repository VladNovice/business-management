# fastapi imports
from fastapi import APIRouter
from fastapi import Depends

# sqlalchemy imports
from sqlalchemy.ext.asyncio import AsyncSession

# project imports
from database.models import User
from schemas.user import UserCreate, UserResponce




user_router = APIRouter(prefix='/users', tags=['users'])

@user_router.post("/registred",response_model=UserResponce)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(???),

):
    existing_user = await db.execute