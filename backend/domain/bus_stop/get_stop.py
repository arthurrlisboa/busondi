from backend.domain.bus_stop.get_stop_impl import GetStopImpl

class GetStop:
    
    def __init__(self):
        self.impl = GetStopImpl()

    def get_all_stops(self):
        return self.impl.get_all_stops_impl()

    def get_stop_by_id(self, stop_id):
        return self.impl.get_stop_by_id_impl(stop_id)

    def get_stops_coordinates(self, stops_list):
        return self.impl.get_stops_coordinates_impl(stops_list)

    def get_stops_from_route(self, route_id):
        return self.impl.get_stops_from_route_impl(route_id)