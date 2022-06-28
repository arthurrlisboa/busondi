from backend.domain.repositories.route_stop_repository import RouteStopRepository
from backend.domain.repositories.stops_repository import StopsRepository
from backend.domain.bus_stop.get_stop_impl import GetStopImpl

class GetStop:
    
    def __init__(self, stops_repo=None, route_stop_repo=None):
        if(stops_repo is None and route_stop_repo is None):
            self.impl = GetStopImpl(StopsRepository(), RouteStopRepository())
        else:
            self.impl = GetStopImpl(stops_repo, route_stop_repo)

    def get_all_stops(self):
        return self.impl.get_all_stops_impl()

    def get_stop_by_id(self, stop_id):
        return self.impl.get_stop_by_id_impl(stop_id)

    def get_stops_coordinates(self, stops_list):
        return self.impl.get_stops_coordinates_impl(stops_list)

    def get_stops_from_route(self, route_id):
        return self.impl.get_stops_from_route_impl(route_id)