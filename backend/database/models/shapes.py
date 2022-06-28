from sqlalchemy import Column, String
from geoalchemy2.types import Geometry

from backend.database.config.db_base import Base


class Shapes(Base):

    __tablename__ = 'shapes'

    shape_id = Column(String, primary_key=True)
    polygon = Column(String)
    

    def __repr__(self):
        return f'Shapes: {self.polygon}'