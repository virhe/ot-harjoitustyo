import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.entities.base import Base


@pytest.fixture(scope="session")
def engine():
    # Run in memory (avoids dealing with directories! yay!)
    return create_engine("sqlite:///:memory:")


@pytest.fixture(scope="session")
def handle_tables(engine):
    # Create all tables from Base children
    Base.metadata.create_all(engine)

    yield

    # Drop all tables (run after all tests)
    Base.metadata.drop_all(engine)


@pytest.fixture()
def session(engine, handle_tables):
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    # Close session after all tests
    session.close()
    transaction.rollback()
    connection.close()
