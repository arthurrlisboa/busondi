from backend.domain.route_stop.get_route_stop_impl import GetRouteStopImpl

class GetRouteStop:

    def __init__(self):
        self.impl = GetRouteStopImpl()

    def get_coordinates_stops_in_route(self, route_id):
        return self.impl.get_coordinates_stops_in_route_impl(route_id)