# projects.py
from fastapi import APIRouter, HTTPException
from fastapi import Depends

from app.backend.schemas.project import ProjectBase, ProjectResponse, ProjectCreate, ProjectUpdate
from app.backend.database.models import Project, User
from app.backend.database.base import get_db_session
from app.backend.core.security import get_current_user

from sqlalchemy.ext.asyncio import AsyncSession
project_router = APIRouter(prefix="/projects", tags=["projects"])


@project_router.post("/create", response_model=ProjectResponse)
async def creating_project(
    project_data: ProjectCreate,
    db: AsyncSession = Depends(get_db_session), 
    current_user: User = Depends(get_current_user)
):
    payload = project_data.model_dump(exclude_unset=True)
    new_project = Project(**payload, user_id=current_user.id)

    db.add(new_project)
    await db.commit()
    await db.refresh(new_project)

    return new_project

