from backend.domain.repositories.stops_repository import StopsRepository

class BusStopsImpl:

    stop_id = ''
    stop_name = ''
    stop_lat = 0.0
    stop_lon = 0.0

    def __init__(self, stop_id, stop_name, stop_lat, stop_lon):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon

    def get_all_stops():
        all_stops = StopsRepository.get_all_stops_repo()
        stops_list = []
        for stop in all_stops:
            stops_list.append(BusStopsImpl(stop.stop_id, stop.stop_name, stop.stop_lat, stop.stop_lon))
        return stops_list

    def get_stop_by_id(stop_id):
        stop_repo = StopsRepository.get_stop_by_id_repo(stop_id)
        stop_class = BusStopsImpl(stop_repo.stop_id, stop_repo.stop_name, stop_repo.stop_lat, stop_repo.stop_lon)
        return stop_class