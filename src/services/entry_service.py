from src.entities.entry import Entry


class EntryService:
    """
    Responsible for managing all entries.

    Attributes:
        entry_repository: Handles database operations for all entries.
    """

    def __init__(self, entry_repository):
        self.entry_repository = entry_repository

    def add_entry(self, user_id, entry_type, amount, category, date, description):
        entry = Entry(user_id=user_id, type=entry_type, amount=amount,
                      category=category, date=date, description=description)
        self.entry_repository.add_entry(entry)

    # def delete_entry(self, entry_id):
    #     self.entry_repository.delete_entry(entry_id)

    def entries_by_user(self, user_id):
        return self.entry_repository.get_user_entries(user_id)
