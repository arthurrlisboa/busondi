from backend.adapters.route_stop_repository_impl import RouteStopRepositoryImpl

class RouteStopRepository:
    def __init__(self, repo=None):
        if(repo is None):
            self.repo = RouteStopRepositoryImpl()
        else:
            self.repo = repo

    def return_all_stops_in_route(self, route_id):
        return self.repo.return_all_stops_in_route_impl(route_id)