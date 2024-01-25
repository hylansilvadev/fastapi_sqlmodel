from typing import List, Optional

from sqlmodel import SQLModel

from fastapi_sqlmodel.domains.user.user_schema import UserBase


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class UserUpdate(SQLModel):
    name: Optional[str] = None
    event_id: Optional[int] = None


class UserReadList(SQLModel):
    users: List[UserRead]
