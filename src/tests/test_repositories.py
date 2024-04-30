from datetime import date

import pytest

from src.entities.entry import Entry
from src.entities.user import User
from src.repositories.entry_repository import EntryRepository
from src.repositories.user_repository import UserRepository


# Fixtures
@pytest.fixture
def entry_repository(session):
    return EntryRepository(session)


@pytest.fixture
def user_repository(session):
    return UserRepository(session)


# -----


# EntryRepository
def test_entry_repository_add(session, entry_repository):
    user = User(username="entryreponame", password="entryrepopass")

    session.add(user)
    session.commit()

    entry = Entry(
        user_id=user.id,
        type="Expense",
        amount=2.50,
        category="Bread",
        date=date.today(),
        description="I was very hungry",
    )

    entry_repository.add_entry(entry)

    assert entry.id is not None
    assert entry.user == user


def test_get_entry_id(session, entry_repository):
    user = User(username="entryreponame", password="entryrepopass")

    session.add(user)
    session.commit()

    entry = Entry(
        user_id=user.id,
        type="Income",
        amount=20,
        category="Sales",
        date=date.today(),
        description="",
    )

    session.add(entry)
    session.commit()

    test_entry = entry_repository.get_entry_id(entry.id)

    assert test_entry is not None
    assert test_entry.id == entry.id


def test_entry_delete(session, entry_repository):
    user = User(username="deletionname", password="deletionpass")

    session.add(user)
    session.commit()

    entry = Entry(
        user_id=user.id,
        type="Expense",
        amount=3,
        category="Pepsi",
        date=date.today(),
        description="I was very thirsty",
    )

    entry_repository.add_entry(entry)
    entry_repository.delete_entry(entry.id)

    test_entry = entry_repository.get_entry_id(entry.id)
    assert test_entry is None


def test_entry_delete_invalid(session, entry_repository):
    user = User(username="deletionname", password="deletionpass")

    session.add(user)
    session.commit()

    try:
        entry_repository.delete_entry(1337)
        # If no error is raised
        success = True
    except Exception:
        success = False

    assert success


# -----


# UserRepository
def test_user_repository_add(session, user_repository):
    user = User(username="testuserreponame", password="testuserrepopass")

    user_repository.add_user(user)

    assert user.id is not None


def test_get_user_entries(session, entry_repository):
    user = User(username="testuserreponame", password="entryrepopass")

    session.add(user)
    session.commit()

    entry = Entry(
        user_id=user.id,
        type="Income",
        amount=20,
        category="Sales",
        date=date.today(),
        description="",
    )

    entry2 = Entry(
        user_id=user.id,
        type="Expense",
        amount=13,
        category="Candies",
        date=date.today(),
        description="Yum",
    )

    session.add(entry)
    session.add(entry2)
    session.commit()

    test_entries = entry_repository.get_user_entries(user.id)

    assert test_entries is not None
    assert len(test_entries) == 2


def test_find_user_name(session, user_repository):
    user = User(username="testuserreponame", password="testuserrepopass")

    session.add(user)
    session.commit()

    result = user_repository.find_user_name(user.username)
    assert result is not None
    assert result.username == user.username


# -----
