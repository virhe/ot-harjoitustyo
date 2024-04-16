
class Entry:
    """ A class to represent a budgeting Entry """
    def __init__(self, amount: float, category: str, description: str, date: str) -> None:
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
