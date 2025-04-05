import uvicorn
from fastapi import FastAPI
from app.database.base import setup_database
from app.core.config import Config as cfg
from app.api.routers.users import user_router

from contextlib import asynccontextmanager




@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db_sessionmaker = await setup_database(cfg.db_url)
    yield

app = FastAPI(title="business statistics app", lifespan=lifespan)

app.include_router(router=user_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)