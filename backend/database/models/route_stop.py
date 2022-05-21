from sqlalchemy import Column, Float, String, ForeignKey, Integer

from backend.database.config.db_base import Base


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
