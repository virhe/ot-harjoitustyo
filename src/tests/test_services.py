from unittest.mock import MagicMock

import pytest

from src.services.entry_service import EntryService
from src.services.user_service import UserService


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


# -----


# TODO user_service tests
