from fastapi import APIRouter, Depends
from sqlmodel import Session

from fastapi_sqlmodel.database.database import get_db
from fastapi_sqlmodel.domains.user.user_model import UserCreate, UserRead
from fastapi_sqlmodel.domains.user.user_schema import User

users = APIRouter(prefix='/user', tags=['User'])


@users.post('/', response_model=UserRead)
def create_user(*, session: Session = Depends(get_db), user: UserCreate):
    user_db = User.model_validate(user)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db
