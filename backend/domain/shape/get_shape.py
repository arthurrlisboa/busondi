from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.repositories.shapes_repository import ShapesRepository
from backend.domain.shape.get_shape_impl import GetShapeImpl

class GetShape:
    
    def __init__(self, routes_repo=None, shapes_repo=None):
        if(routes_repo is None and shapes_repo is None):
            self.impl = GetShapeImpl(RoutesRepository(), ShapesRepository())
        else:
            self.impl = GetShapeImpl(routes_repo, shapes_repo)
    
    def get_polygon(self, route_id):
        return self.impl.get_polygon_impl(route_id)