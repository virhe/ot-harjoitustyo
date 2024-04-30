from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    """
    Represents a user

    Attributes
        id: Integer, unique identifier
        username: String, username of the user
        password: String, password of the user

    A relationship between "User" and "Entry" is also created
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    entries = relationship("Entry", back_populates="user")
