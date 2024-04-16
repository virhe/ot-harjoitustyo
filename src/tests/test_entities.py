from datetime import date
from src.entities.user import User
from src.entities.entry import Entry


def test_add_user(session):
    user = User(username="testusername", password="testpassword")

    session.add(user)
    session.commit()

    assert user.id is not None


def test_add_entry(session):
    user = User(username="entryusername", password="entrypassword")

    session.add(user)
    session.commit()

    entry = Entry(user_id=user.id, amount=2.50, category="Bread", date=date.today(), description="I was very hungry")
    session.add(entry)
    session.commit()

    assert entry.id is not None
    assert entry.user == user

