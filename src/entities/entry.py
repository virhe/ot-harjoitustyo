from sqlalchemy import Column, Integer, Float, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from .base import Base


class Entry(Base):
    """
    Represents a financial entry.

    Fields:
    - id (Integer)
    - user_id (Integer)
    - amount (Float)
    - category (String)
    - date (Date)
    - description (Text)
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
