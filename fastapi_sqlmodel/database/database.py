from sqlmodel import Session, SQLModel, create_engine

from ..core.settings import settings

connect_args = {'check_same_thread': False}

ENGINE = create_engine(
    settings.DATABASE_DEVELOPMENT,
    echo=settings.DATABASE_DEVELOPMENT_ECHO,
    connect_args=connect_args,
)


def create_db_and_tables():
    SQLModel.metadata.create_all(ENGINE)


def get_db():
    with Session(ENGINE) as session:
        yield session
