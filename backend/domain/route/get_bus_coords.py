from backend.domain.repositories.real_time_repository import RealTimeRepository
from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.route.get_bus_coords_impl import GetBusCoordsImpl

class GetBusCoords:

    def __init__(self, routes_repo=None, real_time_repo=None):
        if(routes_repo is None and real_time_repo is None):
            self.impl = GetBusCoordsImpl(RoutesRepository(), RealTimeRepository())
        else:
            self.impl = GetBusCoordsImpl(routes_repo, real_time_repo)
    
    def get_bus_coords(self, route_id):
        return self.impl.get_bus_coords_impl(route_id)