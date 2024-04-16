
class Entry:
    """ A class to represent a budgeting Entry

     Attributes:
         amount (float): The amount of currency
         category (str): The category of the entry
         description (str): The description of the entry
         date (str): The date of the entry
    """

    def __init__(self, amount: float, category: str, description: str, date: str) -> None:
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
