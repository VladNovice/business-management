from pydantic import BaseModel
from database.models import Project


class Project(BaseModel):
    id: int
    name: str
    money_day: int