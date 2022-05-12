from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from .db_base import Base
from backend.database.models import bus_departures, bus_stops, routes, route_stop, shapes, user, favorites


def init_database():
    engine = create_engine('sqlite:///./backend/database.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    session.close()