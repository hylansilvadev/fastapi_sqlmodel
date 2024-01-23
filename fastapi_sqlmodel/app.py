from fastapi import FastAPI

from .database.database import create_db_and_tables
from .domains.event.event_route import events
from .domains.user.user_route import users

app = FastAPI()

app.include_router(events)
app.include_router(users)


@app.on_event('startup')
def create_engine():
    create_db_and_tables()


@app.get('/', tags=["Default Route"])
async def root() -> str:
    return 'Bem vindo ao FastAPI + SQLModel, por: Hylan Silva'
