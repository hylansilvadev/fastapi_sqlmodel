from sqlmodel import SQLModel


class EventCreate(SQLModel):
    event_name: str
    event_description: str


class EventRead(SQLModel):
    id: int
    event_name: str
    evenrt_description: str
