from fastapi_sqlmodel.domains.user.user_schema import UserBase


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
