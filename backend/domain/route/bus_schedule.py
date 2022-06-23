from backend.domain.route.bus_schedule_impl import BusScheduleImpl

class BusSchedule:

    def __init__(self):
        self.impl = BusScheduleImpl()

    def get_arrival_time(self, stop_id, route_id):
        return self.impl.get_arrival_time_impl(stop_id, route_id)

    def order_by_arrival_time(self, stop_routes):
        return self.impl.order_by_arrival_time_impl(stop_routes)