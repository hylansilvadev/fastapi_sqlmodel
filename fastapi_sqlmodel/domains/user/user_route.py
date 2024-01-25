from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from fastapi_sqlmodel.database.database import get_db
from fastapi_sqlmodel.domains.user.user_model import (
    UserCreate,
    UserRead,
    UserReadList,
    UserUpdate,
)
from fastapi_sqlmodel.domains.user.user_schema import User

users = APIRouter(prefix='/user', tags=['User'])


@users.post('/', response_model=UserRead)
def create_new_user(*, session: Session = Depends(get_db), user: UserCreate):
    user_db = User.model_validate(user)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db


@users.get('/{user_id}', response_model=UserRead)
def get_user_by_user_id(*, session: Session = Depends(get_db), user_id: int):
    query = session.get(User, user_id)
    if not query:
        raise HTTPException(status_code=404, detail='User not found.')
    return query


@users.get('/', response_model=UserReadList)
def read_all_users(
    *,
    session: Session = Depends(get_db),
    offset: int = 0,
    limit: int = Query(default=100, le=100)
):
    users_list = session.exec(select(User).offset(offset).limit(limit)).all()
    return {'users': users_list}


@users.patch('/{user_id}', response_model=UserRead)
def update_hero_by_id(
    *, session: Session = Depends(get_db), user_id: int, user: UserUpdate
):
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    user_data = user.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@users.delete('/{user_id}')
def delete_user_by_id(*, session: Session = Depends(get_db), user_id: int):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    session.delete(user)
    session.commit()
    return {'ok': True}
