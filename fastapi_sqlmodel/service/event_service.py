from sqlmodel import Session
from ..database.schemas.event_schema import Event
from ..database.models.event_model import EventCreate
from ..database.database import engine


def create_new_event(event: EventCreate):
    with Session(engine) as session:
        thread = Event.model_validate(event)
        print("resultado da thread", thread)
        session.add(thread)
        session.commit()
        session.refresh(thread)
        return thread
