#!/usr/bin/python3
"""
Definition of class State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base and links to the MySQL table states

    Attributes:
        id (int): The state id. Auto-generated, unique, primary key
        name (str): The state name. String with max 128 chars, not null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
