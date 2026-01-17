#!/usr/bin/python3
"""Add the State object 'Louisiana' to the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # إنشاء كائن جديد من نوع State
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
