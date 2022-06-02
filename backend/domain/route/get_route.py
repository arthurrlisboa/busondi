from backend.domain.route.get_route_impl import GetRouteImpl

class GetRoute:
    def get_routes_from_stop(stop_id):
        return GetRouteImpl.get_routes_from_stop_impl(stop_id)