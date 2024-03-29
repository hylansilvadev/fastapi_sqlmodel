from typing import Optional
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    name: str = Field(index=True)
    event_id: Optional[int | None] = Field(
        default=None, foreign_key='event.id')


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
