from src.entities.entry import Entry
from src.database import session


class EntryRepository:
    def __init__(self):
        self.session = session

    def add_entry(self, entry):
        self.session.add(entry)
        self.session.commit()

    def delete_entry(self, entry_id):
        entry = self.get_entry_id(entry_id)
        self.session.delete(entry)
        self.session.commit()

    def get_entry_id(self, entry_id):
        entry = self.session.query(Entry).filter_by(id=entry_id).first()
        return entry

    def get_user_entries(self, user_id):
        return self.session.query(Entry).filter_by(user_id=user_id).all()
