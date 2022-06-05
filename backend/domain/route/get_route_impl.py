from domain.repositories.routes_repository import RoutesRepository
from domain.route.route import Route

class GetRouteImpl:

    def get_routes_from_stop_impl(stop_id):
        stop_routes_list = []
        all_routes_from_stop = RoutesRepository.return_all_routes_from_stop(stop_id)
        for entry in all_routes_from_stop:
            route = RoutesRepository.return_one_route_by_id(entry.route_id)
            stop_routes_list.append([entry.route_stop_id, Route(entry.route_id, route.route_short_name)])
        return stop_routes_list

    def get_all_routes_impl():
        all_routes = RoutesRepository.return_all_routes()
        routes_list = []
        for route in all_routes:
            routes_list.append(Route(route.route_id, route.route_short_name, route.route_long_name))
        return routes_list

    def get_route_by_id_impl(route_id):
        route_repo = RoutesRepository.return_route_by_id(route_id)
        route_class = Route(route_repo.route_id, route_repo.route_short_name, route_repo.route_long_name)
        return route_class