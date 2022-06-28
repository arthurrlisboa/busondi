from backend.domain.route_stop.get_route_stop_impl import GetRouteStopImpl
from backend.domain.repositories.route_stop_repository import RouteStopRepository
from backend.domain.bus_stop.get_stop import GetStop

class GetRouteStop:

    def __init__(self, route_stop_repo=None, get_stop=None):
        if(route_stop_repo is None and get_stop is None):
            self.impl = GetRouteStopImpl(RouteStopRepository(), GetStop())
        else:
            self.impl = GetRouteStopImpl(route_stop_repo, get_stop)

    def get_coordinates_stops_in_route(self, route_id):
        return self.impl.get_coordinates_stops_in_route_impl(route_id)