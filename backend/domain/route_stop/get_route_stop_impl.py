from backend.domain.bus_stop.get_stop import GetStop

class GetRouteStopImpl:

    def __init__(self, route_stop_repo):
        self.route_stop_repo = route_stop_repo

    def get_coordinates_stops_in_route_impl(self, route_id):
        route_stops_list = self.route_stop_repo.return_all_stops_in_route(route_id)
        stops_list = []
        for rs in route_stops_list:
            stops_list.append(rs.stop_id)
        stop_coordinates = GetStop().get_stops_coordinates(stops_list)
        return stop_coordinates