from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    """
    Represents a user.

    Fields:
    - id (Integer)
    - username (String)
    - password (String)
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    entries = relationship("Entry", back_populates="user")
