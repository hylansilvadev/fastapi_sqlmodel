from fastapi import FastAPI
from .database.database import create_db_and_tables
from .routes.event_route import events
app = FastAPI()

app.include_router(events)


@app.on_event("startup")
def create_engine():
    create_db_and_tables()


@app.get('/')
async def root() -> str:
    return 'Bem vindo ao FastAPI + SQLModel, por: Hylan Silva'
