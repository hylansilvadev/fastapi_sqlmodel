from typing import Optional

from sqlmodel import Field, SQLModel


class UserEventLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key='user.id', primary_key=True
    )
    event_id: Optional[int] = Field(
        default=None, foreign_key='event.id', primary_key=True
    )
