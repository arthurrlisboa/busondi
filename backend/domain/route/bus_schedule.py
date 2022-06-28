from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.repositories.route_stop_repository import RouteStopRepository
from backend.domain.route.bus_schedule_impl import BusScheduleImpl

class BusSchedule:

    def __init__(self, routes_repo=None, route_stop_repo=None):
        if(routes_repo is None and route_stop_repo is None):
            self.impl = BusScheduleImpl(RoutesRepository(), RouteStopRepository(), False)
        else:
            self.impl = BusScheduleImpl(routes_repo, route_stop_repo, True)

    def get_arrival_time(self, stop_id, route_id):
        return self.impl.get_arrival_time_impl(stop_id, route_id)

    #def order_by_arrival_time(self, stop_routes):
        #return self.impl.order_by_arrival_time_impl(stop_routes)