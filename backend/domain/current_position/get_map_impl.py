from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.repositories.shapes_repository import ShapesRepository

class GetMapImpl:

    def get_actual_map_impl(route_id):
        route = RoutesRepository.return_one_route_by_id(route_id)
        route_number = RoutesRepository.return_route_conversion(route_id)
        polygon_shape = ShapesRepository.return_shape_by_id(route.shape_id)
        return [route_number, polygon_shape]
