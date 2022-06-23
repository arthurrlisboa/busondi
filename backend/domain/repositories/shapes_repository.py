from backend.adapters.shapes_repository_impl import ShapesRepositoryImpl

class ShapesRepository:

    def __init__(self, repo=None):
        if(repo is None):
            self.repo = ShapesRepositoryImpl()
        else:
            self.repo = repo
    
    def return_shape_by_id(self, shape_id):
        return self.repo.return_shape_by_id_impl(shape_id)