#!/usr/bin/python3
"""Query table in database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    res = (session.query(State).
           filter(State.name.ilike('%a%')).
           order_by(State.id))
    for inst in res:
        session.delete(inst)
    else:
        session.commit()
