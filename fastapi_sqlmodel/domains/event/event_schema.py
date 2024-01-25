from typing import Optional

from sqlmodel import Field, SQLModel


class EventBase(SQLModel):
    event_name: str = Field(index=True)
    event_description: str
    owner_id: Optional[int | None] = Field(default=None, foreign_key='user.id')


class Event(EventBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

