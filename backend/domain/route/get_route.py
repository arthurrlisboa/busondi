from backend.domain.route.get_route_impl import GetRouteImpl

class GetRoute:

    def __init__(self):
        self.impl = GetRouteImpl()

    def get_routes_from_stop(self, stop_id):
        return self.impl.get_routes_from_stop_impl(stop_id)

    def get_all_routes(self):
        return self.impl.get_all_routes_impl()

    def get_route_by_id(self, route_id):
        return self.impl.get_route_by_id_impl(route_id)