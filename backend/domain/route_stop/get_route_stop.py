from backend.domain.route_stop.get_route_stop_impl import GetRouteStopImpl
from backend.domain.repositories.route_stop_repository import RouteStopRepository

class GetRouteStop:

    def __init__(self, route_stop_repo=None):
        if(route_stop_repo is None):
            self.impl = GetRouteStopImpl(RouteStopRepository())
        else:
            self.impl = GetRouteStopImpl(route_stop_repo)

    def get_coordinates_stops_in_route(self, route_id):
        return self.impl.get_coordinates_stops_in_route_impl(route_id)