from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .db_base import Base
from backend.database.models import bus_stops

def init_database():
    engine = create_engine('sqlite:///./sqlite3.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    session.close()