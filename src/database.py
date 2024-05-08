from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .config import DATABASE_URL
from .entities.base import Base

default_engine = create_engine(DATABASE_URL, echo=True)
session = Session(bind=default_engine)


# Create database tables based on children classes of Base
def init_db(engine=default_engine):
    Base.metadata.create_all(engine)
