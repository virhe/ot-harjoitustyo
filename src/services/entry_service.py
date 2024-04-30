from src.entities.entry import Entry


class EntryService:
    """Responsible for the logic related to entries
    """

    def __init__(self, entry_repository):
        """Constructor

        Args:
            entry_repository: entry_repository instance
        """

        self.entry_repository = entry_repository

    def add_entry(self, user_id, entry_type, amount, category, date, description):
        """Handles adding a new entry

        Args:
            user_id: user id of the user who created the entry
            entry_type: type of entry ("Income", "Expense")
            amount: value of the entry
            category: category of the entry
            date: date of the entry
            description: description of the entry
        """

        entry = Entry(
            user_id=user_id,
            type=entry_type,
            amount=amount,
            category=category,
            date=date,
            description=description,
        )
        self.entry_repository.add_entry(entry)

    # def delete_entry(self, entry_id):
    #     self.entry_repository.delete_entry(entry_id)

    def entries_by_user(self, user_id):
        """Returns all entries by given user id

        Args:
            user_id: user id of the user who created the entries
        """

        return self.entry_repository.get_user_entries(user_id)
