from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Float

db_bus_stops = SQLAlchemy()

class BusStops(db_bus_stops.Model):

    __tablename__ = 'bus_stops'

    stop_id = Column(String, primary_key=True)
    stop_name =  Column(String)
    stop_lat = Column(Float)
    stop_lon = Column(Float)

    def __init__(self, stop_id, stop_name, stop_lat, stop_lon):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon