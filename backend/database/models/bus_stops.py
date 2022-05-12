from sqlalchemy import Column, String, Float
from backend.app import busondi_database

from backend.database.config.db_base import Base


class BusStops(busondi_database.Model):

    __tablename__ = 'bus_stops'

    stop_id = Column(String, primary_key=True)
    stop_name =  Column(String)
    stop_lat = Column(Float)
    stop_lon = Column(Float)

    def __repr__(self):
        return f'BusStop {self.stop_name}'

    '''
    def __init__(self, stop_id, stop_name, stop_lat, stop_lon):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon
    '''