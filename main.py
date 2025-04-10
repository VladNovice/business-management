import uvicorn
from fastapi import FastAPI
from app.backend.database.base import setup_database
from app.backend.core.config import Config as cfg

#routers
from app.backend.api.routers.users import user_router
from app.backend.api.routers.projects import project_router
from contextlib import asynccontextmanager




@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db_sessionmaker = await setup_database(cfg.db_url)
    yield

app = FastAPI(title="business statistics app", lifespan=lifespan)

app.include_router(router=user_router)
app.include_router(router=project_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)