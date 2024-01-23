from typing import Optional

from sqlmodel import Field, SQLModel

# from .user_event_link_schema import UserEventLink

# if TYPE_CHECKING:
#     from .event_schema import Event


class UserBase(SQLModel):
    name: str = Field(index=True)

    # events: List['Event'] = Relationship(
    #     back_populates='users', link_model=UserEventLink
    # )


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
