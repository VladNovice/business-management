from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Request

class Base(DeclarativeBase):
    pass

async def setup_database(database_url):
    engine = create_async_engine(database_url, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return async_sessionmaker(engine, expire_on_commit=True)

async def get_db_session(requests: Request) -> AsyncSession:
    session_maker = requests.app.state.db_sessionmaker
    async with session_maker() as session:
        yield session