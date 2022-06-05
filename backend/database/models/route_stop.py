from sqlalchemy import Column, Float, String, ForeignKey, Integer

from database.config.db_base import Base


class RouteStop(Base):

    __tablename__ = 'route_stop'

    route_stop_id = Column(Integer, primary_key = True)
    route_id = Column(String, ForeignKey('routes.route_id'))
    stop_id = Column(String, ForeignKey('bus_stops.stop_id'))
    stop_sequence = Column(Integer)
    traveled_dist = Column(Float)
    traveled_time = Column(Float)

    def __repr__(self):
        return f'RouteStop {self.route_stop_id}'

    def __init__(self, route_stop_id, route_id, stop_id, stop_sequence, traveled_dist, traveled_time):
        self.route_stop_id = route_stop_id
        self.route_id = route_id
        self.stop_id = stop_id
        self.stop_sequence = stop_sequence
        self.traveled_dist = traveled_dist
        self.traveled_time = traveled_time
