#!/usr/bin/python3
"""
A python file that contains the class definition of a State and an instance
"""
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):

    '''A state definition'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":

    engine = create_engine('mysql:{}:{}//@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
