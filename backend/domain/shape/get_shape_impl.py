from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.repositories.shapes_repository import ShapesRepository

import shapely

class GetShapeImpl:
    
    def get_polygon_impl(route_id):
        route = RoutesRepository.return_one_route_by_id(route_id)
        polygon_shape = ShapesRepository.return_shape_by_id(route.shape_id)
        return shapely.wkt.loads(polygon_shape)