from backend.database.config.db_connection import DBConnection
from backend.database.models.shapes import Shapes

class ShapesRepositoryImpl:

    def __init__(self):
        self.conn = DBConnection()

    def return_shape_by_id_impl(self, shape_id):
        with self.conn as connection:
            shape = connection.session.query(Shapes).filter_by(shape_id=shape_id).first()
        return shape.polygon