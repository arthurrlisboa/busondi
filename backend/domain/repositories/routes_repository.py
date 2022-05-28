from backend.adapters.routes_repository_impl import RoutesRepositoryImpl

class RoutesRepository:

    def get_routes_from_stop_repo(stop_id):
        return RoutesRepositoryImpl.get_routes_from_stop_repo_(stop_id)
      
    def get_route_stop_from_ids_repo(stop_id, route_id):
        return RoutesRepositoryImpl.get_route_stop_from_ids_repo_(stop_id, route_id)
    
    def get_trips_from_route_repo(route_id):
        return RoutesRepositoryImpl.get_trips_from_route_repo_(route_id)