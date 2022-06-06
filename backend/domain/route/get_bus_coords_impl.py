from backend.domain.repositories.real_time_repository import RealTimeRepository
from backend.domain.repositories.routes_repository import RoutesRepository

class GetBusCoordsImpl:

    def get_bus_coords_impl(route_id):
        route_number = RoutesRepository.return_route_conversion(route_id)
        bus_coords = RealTimeRepository.get_real_time_bus_coords(int(route_number))
        return bus_coords