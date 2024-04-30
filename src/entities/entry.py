from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship

from .base import Base


class Entry(Base):
    """Represents a financial entry

    Attributes
        id: Integer, unique identifier
        user_id: Integer, represents the user who created the entry
        type: String, "Income" or "Expense"
        amount: Float, represents the value of the entry
        category: String, represents the category of the entry
        date: Date, represents the date of the entry
        description: String, represents the description of the entry

    A relationship between "User" and "Entry" is also created
    """

    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    description = Column(Text)

    user = relationship("User", back_populates="entries")
