from backend.adapters.route_stop_repository_impl import RouteStopRepositoryImpl

class RouteStopRepository:
    def __init__(self, repo=None):
        if(repo is None):
            self.repo = RouteStopRepositoryImpl()
        else:
            self.repo = repo

    def return_all_stops_in_route(self, route_id):
        return self.repo.return_all_stops_in_route_impl(route_id)

    def return_all_routes_from_stop(self, stop_id):
        return self.repo.return_all_routes_from_stop_impl(stop_id)
      
    def return_route_stop_by_id(self, stop_id, route_id):
        return self.repo.return_route_stop_by_id_impl(stop_id, route_id)