from domain.repositories.route_stop_repository import RouteStopRepository
from domain.bus_stop.get_stop import GetStop

class GetRouteStopImpl:
    def get_coordinates_stops_in_route_impl(route_id):
        route_stops_list = RouteStopRepository.return_all_stops_in_route(route_id)
        stops_list = []
        for rs in route_stops_list:
            stops_list.append(rs.stop_id)
        stop_coordinates = GetStop.get_stops_coordinates(stops_list)
        return stop_coordinates