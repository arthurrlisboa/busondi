from backend.domain.route.get_route_impl import GetRouteImpl

class GetRoute:
    def get_routes_from_stop(stop_id):
        return GetRouteImpl.get_routes_from_stop_impl(stop_id)

    def get_all_routes():
        return GetRouteImpl.get_all_routes_impl()

    def get_route_by_id(route_id):
        return GetRouteImpl.get_route_by_id_impl(route_id)