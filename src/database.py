from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .config import DATABASE_URL
from .entities.base import Base


engine = create_engine(DATABASE_URL, echo=True)
session = Session(bind=engine)


def init_db():
    Base.metadata.create_all(engine)
