from backend.adapters.routes_repository_impl import RoutesRepositoryImpl

class RoutesRepository:

    def __init__(self, repo=None):
        if(repo is None):
            self.repo = RoutesRepositoryImpl()
        else:
            self.repo = repo

    def return_all_routes_from_stop(self, stop_id):
        return self.repo.return_all_routes_from_stop_impl(stop_id)
      
    def return_route_stop_by_id(self, stop_id, route_id):
        return self.repo.return_route_stop_by_id_impl(stop_id, route_id)
    
    def return_trips_from_route(self, route_id):
        return self.repo.return_trips_from_route_impl(route_id)
    
    def return_one_route_by_id(self, route_id):
        return self.repo.return_one_route_by_id_impl(route_id)
    
    def return_route_conversion(self, route_id):
        return self.repo.return_route_conversion_impl(route_id)

    def return_all_routes(self):
        return self.repo.return_all_routes_impl()

    def return_route_by_id(self, route_id):
        return self.repo.return_route_by_id_impl(route_id)