#!/usr/bin/python3
"""Query table in database
"""
import sys
from model_city import City
from model_state import State, Base

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    res = (session.query(City, State).join(State).
           order_by(City.id).all())
    print(res)
    for joint in res:
        print('{}: ({}) {}'.format(joint[1].name, joint[0].id, joint[0].name))
