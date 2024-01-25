from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from fastapi_sqlmodel.database.database import get_db
from fastapi_sqlmodel.domains.event.event_model import (
    EventCreate,
    EventRead,
    EventReadList,
    EventUpdate,
)
from fastapi_sqlmodel.domains.event.event_schema import Event

events = APIRouter(prefix='/event', tags=['Event'])


@events.post('/', response_model=EventRead)
def create_new_event(
    *, session: Session = Depends(get_db), event: EventCreate
):
    event_db = Event.model_validate(event)
    session.add(event_db)
    session.commit()
    session.refresh(event_db)
    return event_db


@events.get('/{event_id}', response_model=EventRead)
def get_event_by_event_id(
    *, session: Session = Depends(get_db), event_id: int
):
    query = session.get(Event, event_id)
    if not query:
        raise HTTPException(status_code=404, detail='Event not found')
    return query


@events.get('/', response_model=EventReadList)
def read_all_events(
    *,
    session: Session = Depends(get_db),
    offset: int = 0,
    limit: int = Query(default=100, le=100)
):
    events_list = session.exec(select(Event).offset(offset).limit(limit)).all()
    return {'events': events_list}


@events.patch('/{event_id}', response_model=EventRead)
def update_hero_by_id(
    *, session: Session = Depends(get_db), event_id: int, event: EventUpdate
):
    db_event = session.get(Event, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail='Event not found')
    event_data = event.model_dump(exclude_unset=True)
    for key, value in event_data.items():
        setattr(db_event, key, value)
    session.add(db_event)
    session.commit()
    session.refresh(db_event)
    return db_event


@events.delete('/{event_id}')
def delete_event_by_id(*, session: Session = Depends(get_db), event_id: int):
    event = session.get(Event, event_id)
    if not event:
        raise HTTPException(status_code=404, detail='Event not found')
    session.delete(event)
    session.commit()
    return {'ok': True}
