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
        server_default=func.now()  # Значение по умолчанию при создании
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),  # Добавлено значение по умолчанию
        onupdate=func.now()         # Обновление при изменении записи
    )



class User(Base, TimeStampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password_hash: Mapped[str] = mapped_column(String(128))



    def set_password(self, password: str):
            self.password_hash = pwd_context.hash(password)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)
    

class Project(Base, TimeStampMixin):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    money_day: Mapped[int] = mapped_column(Integer)



class Revenue(Base, TimeStampMixin):
    __tablename__ = "revenues"
    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey('projects.id'))
    data: Mapped[datetime] = mapped_column(Date, nullable=False)
    amount: Mapped[int] = mapped_column(nullable=False)

    project = relationship("Project", back_populates="revenues")

Project.revenues = relationship("Revenue", back_populates="project")
