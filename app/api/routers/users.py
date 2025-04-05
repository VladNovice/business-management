# fastapi imports
from fastapi import APIRouter, HTTPException
from fastapi import Depends

# sqlalchemy imports
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

# project imports
from database.models import User
from schemas.user import UserCreate, UserResponce, Token
from database.base import get_db_session
from core.security import verify_password, status, create_access_token, timedelta, ACCESS_TOKEN_EXPIRE_MINUTES

# other 




user_router = APIRouter(prefix='/users', tags=['users'])




@user_router.post("/registred", response_model=Token)


@user_router.post("/login", response_model=Token)
async def login_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db_session),
):
    result = await db.execute(select(User).where(User.name == user_data.name))
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(
        data={"sub": user.name},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

