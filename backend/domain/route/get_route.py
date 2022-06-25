from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.repositories.route_stop_repository import RouteStopRepository
from backend.domain.route.get_route_impl import GetRouteImpl

class GetRoute:

    def __init__(self, routes_repo=None, route_stop_repo=None):
        if(routes_repo is None and route_stop_repo is None):
            self.impl = GetRouteImpl(RoutesRepository(), RouteStopRepository())
        else:
            self.impl = GetRouteImpl(routes_repo, route_stop_repo)

    def get_routes_from_stop(self, stop_id):
        return self.impl.get_routes_from_stop_impl(stop_id)

    def get_all_routes(self):
        return self.impl.get_all_routes_impl()

    def get_route_by_id(self, route_id):
        return self.impl.get_route_by_id_impl(route_id)