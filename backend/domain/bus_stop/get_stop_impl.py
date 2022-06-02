from backend.domain.repositories.stops_repository import StopsRepository
from backend.domain.bus_stop.bus_stop import BusStop

class GetStopImpl:

    def get_all_stops():
        all_stops = StopsRepository.get_all_stops_repo()
        stops_list = []
        for stop in all_stops:
            stops_list.append(BusStop(stop.stop_id, stop.stop_name, stop.stop_lat, stop.stop_lon))
        return stops_list

    def get_stop_by_id(stop_id):
        stop_repo = StopsRepository.get_stop_by_id_repo(stop_id)
        stop_class = BusStop(stop_repo.stop_id, stop_repo.stop_name, stop_repo.stop_lat, stop_repo.stop_lon)
        return stop_class