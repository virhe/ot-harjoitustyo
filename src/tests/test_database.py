from sqlalchemy import inspect

from src.database import init_db


def test_database(engine):
    init_db(engine)

    table_names = [table for table in inspect(engine).get_table_names()]

    assert "entries" in table_names
    assert "users" in table_names
