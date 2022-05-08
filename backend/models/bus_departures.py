from tracemalloc import stop
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, ForeignKey, Time

db_bus_departures = SQLAlchemy()

class BusDepartures(db_bus_departures.Model):

    __tablename__ = 'bus_departures'

    trip_id = Column(String, primary_key = True)
    departure_time = Column(Time)
    stop_id = Column(String, ForeignKey('bus_stops.stop_id'))
    route_id = Column(String, ForeignKey('routes.route_id'))

    def __init__(self, trip_id, departure_time, stop_id, route_id):
        self.trip_id = trip_id
        self.departure_time = departure_time
        self.stop_id = stop_id
        self.route_id = route_id