from backend.domain.repositories.routes_repository import RoutesRepository
from backend.domain.route.route import Route

class GetRoute:

    def get_routes_from_stop(stop_id):
        stop_routes_list = []
        all_routes_from_stop = RoutesRepository.get_routes_from_stop_repo(stop_id)
        for entry in all_routes_from_stop:
            route = RoutesRepository.get_route_by_id_repo(entry.route_id)
            stop_routes_list.append([entry.route_stop_id, Route(entry.route_id, route.route_short_name)])
        return stop_routes_list