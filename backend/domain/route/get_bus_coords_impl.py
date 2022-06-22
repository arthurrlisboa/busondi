from backend.domain.repositories.real_time_repository import RealTimeRepository
from backend.domain.repositories.routes_repository import RoutesRepository

class GetBusCoordsImpl:

    def __init__(self, routes_repo=None, real_time_repo=None):
        if(routes_repo is None):
            self.routes_repo = RoutesRepository()
        else:
            self.routes_repo = routes_repo

        if(real_time_repo is None):
            self.real_time_repo = RealTimeRepository()
        else:
            self.real_time_repo = real_time_repo

    def get_bus_coords_impl(self, route_id):
        route_number = self.routes_repo.return_route_conversion(route_id)
        bus_coords = self.real_time_repo.get_real_time_bus_coords(int(route_number))
        return bus_coords