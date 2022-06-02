from backend.domain.bus_stop.get_stop_impl import GetStopImpl

class GetStop:
    def get_all_stops_port():
        return GetStopImpl.get_all_stops()

    def get_stop_by_id_port(stop_id):
        return GetStopImpl.get_stop_by_id(stop_id)