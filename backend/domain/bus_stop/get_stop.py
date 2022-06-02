from backend.domain.bus_stop.get_stop_impl import GetStopImpl

class GetStop:
    def get_all_stops():
        return GetStopImpl.get_all_stops_impl()

    def get_stop_by_id(stop_id):
        return GetStopImpl.get_stop_by_id_impl(stop_id)