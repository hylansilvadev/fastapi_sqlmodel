from typing import Optional

from sqlmodel import Field, SQLModel

# from .user_event_link_schema import UserEventLink

# if TYPE_CHECKING:
#     from ..schemas.user_schema import User


class EventBase(SQLModel):
    event_name: str = Field(index=True)
    event_description: str

    # users: List['User'] = Relationship(
    #     back_populates='events',
    #     link_model=UserEventLink,
    # )


class Event(EventBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
