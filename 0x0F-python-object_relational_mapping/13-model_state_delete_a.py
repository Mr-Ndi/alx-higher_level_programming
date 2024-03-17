#!/usr/bin/python3
"""
Module that connects a python script to a database
"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import  create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    # declaring the vars
    my_host = 'localhost'
    users = sys.argv[1]
    my_password = sys.argv[2]
    my_db = sys.argv[3]
    port = 3306
    
    engine=create_engine('mysql://{}:{}@localhost:3306/{}'.format(users,my_password, my_db))
    session = sessionmaker(bind=engine)
   
    state_to_del = session.query(State).filter(State.name.LIKE ('%a%')).all()
    for state_de in state_to_del:
        session.delete(state_de)
    session.commit()

    session.close()
