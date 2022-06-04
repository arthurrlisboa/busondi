from backend.adapters.route_stop_repository_impl import RouteStopRepositoryImpl

class RouteStopRepository:
    def return_all_stops_in_route(route_id):
        return RouteStopRepositoryImpl.return_all_stops_in_route_impl(route_id)