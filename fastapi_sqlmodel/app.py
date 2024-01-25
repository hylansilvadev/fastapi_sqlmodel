from fastapi import FastAPI

from .core.settings import settings
from .database.database import create_db_and_tables
from .domains.event.event_route import events
from .domains.user.user_route import users

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSSION)

app.include_router(events)
app.include_router(users)


@app.on_event('startup')
def create_engine():
    create_db_and_tables()


@app.get('/', tags=['Default Route'])
async def root() -> str:
    return 'Bem vindo ao FastAPI + SQLModel, por: Hylan Silva'
