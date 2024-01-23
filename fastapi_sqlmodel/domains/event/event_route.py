from fastapi import APIRouter, Depends
from sqlmodel import Session

from fastapi_sqlmodel.database.database import get_db
from fastapi_sqlmodel.domains.event.event_model import EventCreate, EventRead
from fastapi_sqlmodel.domains.event.event_schema import Event

events = APIRouter(prefix='/event', tags=['Event'])


@events.post('/', response_model=EventRead)
def new_event(*, session: Session = Depends(get_db), event: EventCreate):
    event_db = Event.model_validate(event)
    session.add(event_db)
    session.commit()
    session.refresh(event_db)
    return event_db
