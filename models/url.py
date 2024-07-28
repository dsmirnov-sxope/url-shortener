"""
URL Model
"""
from sqlalchemy import Column, Integer, String

from models.base import Base


class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String, unique=True, nullable=False)
    short_url = Column(String, unique=True, nullable=False)
