from datetime import date

from src.entities.entry import Entry
from src.entities.user import User
from src.repositories.entry_repository import EntryRepository
from src.repositories.user_repository import UserRepository


def test_user_repository_add(session):
    user = User(username="testuserreponame", password="testuserrepopass")

    user_repository = UserRepository(session)
    user_repository.add_user(user)

    assert user.id is not None


def test_entry_repository_add(session):
    user = User(username="entryreponame", password="entryrepopass")

    session.add(user)
    session.commit()

    entry = Entry(user_id=user.id, amount=2.50, category="Bread",
                  date=date.today(), description="I was very hungry")

    entry_repository = EntryRepository(session)
    entry_repository.add_entry(entry)

    assert entry.id is not None
    assert entry.user == user
