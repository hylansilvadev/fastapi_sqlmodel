from fastapi import APIRouter

from ..database.models.event_model import EventRead, EventCreate
from ..service.event_service import create_new_event

events = APIRouter(prefix="/event")


@events.post('/', response_model=EventRead)
def new_event(event: EventCreate):
    create_new_event(event)
