from sqlalchemy import Column, ForeignKey, Integer, String, Time

from backend.database.config.db_base import Base


class Favorites(Base):

    __tablename__ = 'favorites'

    favorite_id = Column(Integer, primary_key = True)
    email = Column(String, ForeignKey('user.email'))
    route_id = Column(String, ForeignKey('routes.route_id'))
    stop_id = Column(String, ForeignKey('bus_stops.stop_id'))
    time = Column(Time)          
    notification = Column(String) 

    def __repr__(self):
        return f'Favorites {self.favorite_id}'

    '''
    def __init__(self, favorite_id, email, route_id, stop_id, time, notification):
        self.favorite_id = favorite_id
        self.email = email
        self.route_id = route_id
        self.stop_id = stop_id
        self.time = time
        self.notification = notification
    '''