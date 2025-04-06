# models.py
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import DateTime, Date, func



from datetime import datetime, timezone 
from datetime import date

from passlib.context import CryptContext


from app.backend.database.base import Base


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




class TimeStampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()  
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  
        onupdate=func.now()         
    )



class User(Base, TimeStampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)  
    password_hash: Mapped[str] = mapped_column(String(128))

    projects = relationship("Project", back_populates="owner")


    def set_password(self, password: str):
            self.password_hash = pwd_context.hash(password)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)
    

class Project(Base, TimeStampMixin):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), index=True)  
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    expected_daily_revenue: Mapped[int] = mapped_column(Integer, nullable=True) 
    currency: Mapped[str] = mapped_column(String(10), default='RUB')  
    start_date: Mapped[date] = mapped_column(Date, default=date.today())
    is_active: Mapped[bool] = mapped_column(default=True)
    initial_balance: Mapped[int] = mapped_column(Integer, default=0)  

    owner = relationship("User", back_populates="projects")
    revenues = relationship("Revenue", back_populates="project")

class Revenue(Base, TimeStampMixin):
    __tablename__ = "revenues"
    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'), index=True)
    date: Mapped[datetime] = mapped_column(Date, nullable=False, index=True)  
    income: Mapped[int] = mapped_column(Integer, default=0)
    expenses: Mapped[int] = mapped_column(Integer, default=0)
    category: Mapped[str] = mapped_column(String(50), nullable=True)  
    comment: Mapped[str] = mapped_column(String(200), nullable=True)

    project = relationship("Project", back_populates="revenues")

Project.revenues = relationship("Revenue", back_populates="project")
