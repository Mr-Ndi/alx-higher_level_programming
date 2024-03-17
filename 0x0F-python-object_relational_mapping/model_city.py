#!/usr/bin/python3
"""
A python file that contains the class definition of a State and an instance 
"""
from sqlalchemy import create_engine, PrimaryKeyConstraint, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sys

Base = declarative_base()

class City(Base):
    '''A state definition'''
    __tablename__ = 'cities'
    state_id = Column(Integer, nullable=False, Foreignkey('states.id'))
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__=="__main__":
    engine=create_engine('mysql:{}:{}//@localhost:3306/{}'.format(sys.argv[1],sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
