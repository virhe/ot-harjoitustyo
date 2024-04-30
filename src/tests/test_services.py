from unittest.mock import MagicMock

import bcrypt
import pytest

from src.entities.user import User
from src.services.entry_service import EntryService
from src.services.user_service import (
    UserService,
    UsernameTakenError,
    InvalidUsernameOrPassword,
)


# Fixtures
@pytest.fixture
def entry_repository():
    return MagicMock()


@pytest.fixture
def entry_service(entry_repository):
    return EntryService(entry_repository)


@pytest.fixture
def user_repository():
    return MagicMock()


@pytest.fixture
def user_service(user_repository):
    return UserService(user_repository)


# ------


# EntryService
def test_add_entry(entry_service, entry_repository):
    entry_service.add_entry(1, "Income", 15, "Medicine", "01-01-2001", "test")
    entry_repository.add_entry.assert_called_once()


def test_entries_by_user(entry_service, entry_repository):
    entry_service.entries_by_user(1)
    entry_repository.get_user_entries.assert_called_once_with(1)


def test_delete_entry(entry_service, entry_repository):
    entry_service.delete_entry(1)
    entry_repository.delete_entry.assert_called_once_with(1)


# -----


# UserService
def test_login(user_service, user_repository):
    password = bcrypt.hashpw("loginpass".encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )
    user_repository.find_user_name.return_value = User(
        id=1, username="loginuser", password=password
    )

    assert user_service.login("loginuser", "loginpass") == 1


def test_wrong_login(user_service, user_repository):
    password = bcrypt.hashpw("loginpass".encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )
    user_repository.find_user_name.return_value = User(
        id=1, username="loginuser", password=password
    )

    assert user_service.login("loginuser", "incorrectloginpass") is None


def test_register(user_service, user_repository):
    user_repository.find_user_name.return_value = None
    user_repository.add_user.return_value = 1

    assert user_service.register("registeruser", "registerpass") == 1


def test_register_username_taken(user_service, user_repository):
    user_repository.find_user_name.return_value = User(
        id=1, username="takenname", password="takenpass"
    )

    with pytest.raises(UsernameTakenError):
        user_service.register("takenname", "takenpass")


def test_register_bad_input(user_service, user_repository):
    user_repository.find_user_name.return_value = None

    with pytest.raises(InvalidUsernameOrPassword):
        user_service.register("a", "b")

# -----
