from sqlalchemy import Column, String, ForeignKey, Time

from backend.database.config.db_base import Base


class BusDepartures(Base):

    __tablename__ = 'bus_departures'

    trip_id = Column(String, primary_key = True)
    departure_time = Column(Time)
    stop_id = Column(String, ForeignKey('bus_stops.stop_id'))
    route_id = Column(String, ForeignKey('routes.route_id'))

    def __repr__(self):
        return f'BusDeparture {self.trip_id} at {self.departure_time}'

    '''
    def __init__(self, trip_id, departure_time, stop_id, route_id):
        self.trip_id = trip_id
        self.departure_time = departure_time
        self.stop_id = stop_id
        self.route_id = route_id
    '''