# users.py
# fastapi imports
from fastapi import APIRouter, HTTPException
from fastapi import Depends

# sqlalchemy imports
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

# project imports
from app.database.models import User
from app.schemas.user import UserCreate, UserResponce, Token
from app.database.base import get_db_session
from app.core.security import verify_password, status, create_access_token, timedelta, ACCESS_TOKEN_EXPIRE_MINUTES, get_password_hash

# other 




user_router = APIRouter(prefix='/users', tags=['users'])




@user_router.post("/registred", response_model=Token)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db_session),
):
    ex_user = await db.execute(select(User).where(User.name == user_data.name))
    res_ex_user = ex_user.scalar_one_or_none()

    if res_ex_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Юзернейм уже занят"
        )
    
    new_user = User(
        name=user_data.name,
        password_hash=get_password_hash(user_data.password)
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    access_token = create_access_token(
        data={"sub": new_user.name},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {"access_token": access_token, "token_type": "bearer"}

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

