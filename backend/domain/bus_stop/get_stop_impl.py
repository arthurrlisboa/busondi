from domain.repositories.route_stop_repository import RouteStopRepository
from domain.repositories.stops_repository import StopsRepository
from domain.bus_stop.bus_stop import BusStop

class GetStopImpl:

    def get_all_stops_impl():
        all_stops = StopsRepository.return_all_stops()
        stops_list = []
        for stop in all_stops:
            stops_list.append(BusStop(stop.stop_id, stop.stop_name, stop.stop_lat, stop.stop_lon))
        return stops_list

    def get_stop_by_id_impl(stop_id):
        stop_repo = StopsRepository.return_stop_by_id(stop_id)
        stop_class = BusStop(stop_repo.stop_id, stop_repo.stop_name, stop_repo.stop_lat, stop_repo.stop_lon)
        return stop_class

    def get_stops_coordinates_impl(stops_list):
        stops_in_list = StopsRepository.return_all_stops_in_list(stops_list)
        coordinate_list = []
        for stop in stops_in_list:
            coordinate_list.append((stop.stop_lon, stop.stop_lat))
        return coordinate_list

    def get_stops_from_route_impl(route_id):
        stops_in_route = RouteStopRepository.return_all_stops_in_route(route_id)
        stop_id_list = [stop.stop_id for stop in stops_in_route]
        stops = StopsRepository.return_all_stops_in_list(stop_id_list)
        stops_list = []
        for stop in stops:
            stops_list.append(BusStop(stop.stop_id, stop.stop_name, stop.stop_lat, stop.stop_lon))
        return stops_list