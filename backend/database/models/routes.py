from sqlalchemy import Column, String, ForeignKey

from database.config.db_base import Base


class Routes(Base):

    __tablename__ = 'routes'

    route_id = Column(String, primary_key=True)
    route_short_name = Column(String)
    route_long_name = Column(String)
    shape_id = Column(String, ForeignKey('shapes.shape_id'))
    initial_stop_id = Column(String, ForeignKey('bus_stops.stop_id'))
    final_stop_id = Column(String, ForeignKey('bus_stops.stop_id'))

    def __repr__(self):
        return f'Route {self.route_short_name}'