from backend.domain.route.route import Route

class GetRouteImpl:

    def __init__(self, routes_repo, route_stop_repo):
        self.routes_repo = routes_repo
        self.route_stop_repo = route_stop_repo

    def get_routes_from_stop_impl(self, stop_id):
        stop_routes_list = []
        all_routes_from_stop = self.route_stop_repo.return_all_routes_from_stop(stop_id)
        for entry in all_routes_from_stop:
            route = self.routes_repo.return_one_route_by_id(entry.route_id)
            stop_routes_list.append([entry.route_stop_id, Route(entry.route_id, route.route_short_name)])
        return stop_routes_list

    def get_all_routes_impl(self):
        all_routes = self.routes_repo.return_all_routes()
        routes_list = []
        for route in all_routes:
            routes_list.append(Route(route.route_id, route.route_short_name, route.route_long_name))
        return routes_list

    def get_route_by_id_impl(self, route_id):
        route_repo = self.routes_repo.return_route_by_id(route_id)
        route_class = Route(route_repo.route_id, route_repo.route_short_name, route_repo.route_long_name)
        return route_class