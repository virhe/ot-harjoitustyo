from src.entities.entry import Entry


class EntryRepository:
    """Responsible for database operations related to the Entry class."""

    def __init__(self, session):
        """Constructor

        Args:
            session: sqlalchemy session
        """

        self.session = session

    def add_entry(self, entry):
        """Adds a new entry to the database

        Args:
            entry: Entry instance
        """

        self.session.add(entry)
        self.session.commit()

    def delete_entry(self, entry_id):
        """Deletes an entry from the database

        Args:
            entry_id: id of the entry to be deleted
        """

        entry = self.get_entry_id(entry_id)
        if entry:
            self.session.delete(entry)
            self.session.commit()

    def get_entry_id(self, entry_id):
        """Returns the entry with the given id

        Args:
            entry_id: id of the entry to be returned

        Returns:
            The entry with the given id
        """

        entry = self.session.query(Entry).filter_by(id=entry_id).first()
        return entry

    def get_user_entries(self, user_id):
        """Returns the user entries for the given user_id

        Args:
            user_id: id of the user whose entries to return

        Returns:
            The user entries for the given user_id
        """

        query = self.session.query(Entry).filter_by(user_id=user_id).all()
        return query
