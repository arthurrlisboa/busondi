from sqlalchemy import Column, String, ForeignKey

from backend.database.config.db_base import Base


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

    '''
    def __init__(self, route_id, route_short_name, route_long_name, 
                shape_id, initial_stop_id, final_stop_id):
        self.route_id = route_id
        self.route_short_name = route_short_name
        self.route_long_name = route_long_name
        self.shape_id = shape_id
        self.initial_stop_id = initial_stop_id
        self.final_stop_id = final_stop_id
    '''