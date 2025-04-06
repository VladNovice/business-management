# project.py
from datetime import date
from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    expected_daily_revenue: Optional[int] = None
    currency: str = "RUB"
    start_date: date = date.today()
    is_active: bool = True
    initial_balance: int = 0

class ProjectResponse(ProjectBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass
