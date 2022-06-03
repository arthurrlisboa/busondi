from backend.adapters.shapes_repository_impl import ShapesRepositoryImpl

class ShapesRepository:
    
    def return_shape_by_id(shape_id):
        return ShapesRepositoryImpl.return_shape_by_id_impl(shape_id)