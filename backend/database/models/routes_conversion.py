from sqlalchemy import Column, String

from backend.database.config.db_base import Base


class RoutesConversion(Base):

    __tablename__ = 'routes_conversion'

    route_number = Column(String, primary_key=True)
    route_id = Column(String)

    def __repr__(self):
        return f'Route Converion {self.route_number} - {self.route_id}'