from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.repositories.shapes_repository import ShapesRepository

import shapely

class GetShapeImpl:

    def __init__(self, routes_repo=None, shapes_repo=None):
        if(routes_repo is None):
            self.routes_repo = RoutesRepository()
        else:
            self.routes_repo = routes_repo

        if(shapes_repo is None):
            self.shapes_repo = ShapesRepository()
        else:
            self.shapes_repo = shapes_repo
    
    def get_polygon_impl(self, route_id):
        route = self.routes_repo.return_one_route_by_id(route_id)
        polygon_shape = self.shapes_repo.return_shape_by_id(route.shape_id)
        return shapely.wkt.loads(polygon_shape)