from typing import List, Optional
from sqlmodel import SQLModel
from fastapi_sqlmodel.domains.event.event_schema import EventBase
from fastapi_sqlmodel.domains.user.user_model import UserRead


class EventCreate(EventBase):
    pass


class EventRead(EventBase):
    id: int
    owner: Optional[UserRead] = None


class EventUpdate(SQLModel):
    event_name: Optional[str] = None
    event_description: Optional[str] = None
    owner_id: Optional[int] = None


class EventReadList(SQLModel):
    events: List['EventRead']
