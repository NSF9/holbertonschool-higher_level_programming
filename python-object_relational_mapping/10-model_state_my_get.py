#!/usr/bin/python3
"""Print the State object with the name passed as argument from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == state_name).first()

    if result:
        print(result.id)
    else:
        print("Not found")

    session.close()
