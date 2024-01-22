from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from .user_event_link_schema import UserEventLink
from .user_schema import User


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_name: str = Field(index=True)
    event_description: str
    
    users: List['User'] = Relationship(
        back_populates='events', link_model=UserEventLink
    )
