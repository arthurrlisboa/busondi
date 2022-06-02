from backend.domain.route.bus_schedule_impl import BusScheduleImpl

class BusSchedule:

    def get_arrival_time_port(stop_id, route_id):
        return BusScheduleImpl.get_arrival_time(stop_id, route_id)

    def order_by_arrival_time_port(stop_routes):
        return BusScheduleImpl.order_by_arrival_time(stop_routes)