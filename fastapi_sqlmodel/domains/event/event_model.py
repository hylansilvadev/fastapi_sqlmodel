from fastapi_sqlmodel.domains.event.event_schema import EventBase


class EventCreate(EventBase):
    pass


class EventRead(EventBase):
    id: int
