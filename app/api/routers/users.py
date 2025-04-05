from fastapi import APIRouter

from database.models import User
from schemas.user import User

user_router = APIRouter()

@user_router.post(response_model=)
async def get():
    pass