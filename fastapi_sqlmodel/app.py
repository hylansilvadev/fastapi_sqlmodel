from fastapi import FastAPI
from contextlib import asynccontextmanager

from .core.settings import settings
from .database.database import create_db_and_tables
from .domains.event.event_route import events
from .domains.user.user_route import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSSION,
    lifespan=lifespan,
    docs_url="/docs"
)

app.include_router(events)
app.include_router(users)


@app.get('/', tags=['Default Route'])
async def root() -> str:
    return 'Bem vindo ao FastAPI + SQLModel, por: Hylan Silva'
