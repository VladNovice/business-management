from pydantic import BaseModel

from decimal import Decimal

from datetime import datetime

class UserBase(BaseModel):
    name: str
    
class UserCreate(UserBase):
    password: str

class UserResponce(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode: True

