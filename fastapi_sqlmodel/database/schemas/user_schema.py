from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel
from .user_event_link_schema import UserEventLink

if TYPE_CHECKING:
    from .event_schema import Event


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    events: List["Event"] = Relationship(
        back_populates='users', link_model=UserEventLink
    )
