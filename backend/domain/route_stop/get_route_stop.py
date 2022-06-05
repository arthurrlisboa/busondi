from domain.route_stop.get_route_stop_impl import GetRouteStopImpl

class GetRouteStop:
    def get_coordinates_stops_in_route(route_id):
        return GetRouteStopImpl.get_coordinates_stops_in_route_impl(route_id)