from database.config.db_connection import DBConnection
from database.models.shapes import Shapes

class ShapesRepositoryImpl:

    def return_shape_by_id_impl(shape_id):
        with DBConnection() as connection:
            shape = connection.session.query(Shapes).filter_by(shape_id=shape_id).first()
        return shape.polygon