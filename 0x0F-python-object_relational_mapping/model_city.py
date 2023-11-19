#!/usr/bin/python3

"""a class definition of a City."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()

class City(Base):
    """Ä class City"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
