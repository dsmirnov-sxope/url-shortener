"""
URL Model
"""

from sqlalchemy import Column, Integer, String

from shortener.models.base import Base


class URL(Base):
    """
    Url model
    """

    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String, unique=True, nullable=False)
    short_url = Column(String, unique=True, nullable=False)
