from backend.repository_impl import RepositoryImpl

class Repository:
    def get_all_stops_repo():
        return RepositoryImpl.get_all_stops_repo_()

    def get_stop_by_id_repo(stop_id):
        return RepositoryImpl.get_stop_by_id_repo_(stop_id)

    def get_routes_from_stop_repo(stop_id):
        return RepositoryImpl.get_routes_from_stop_repo_(stop_id)
    
    def get_route_stop_from_ids_repo(stop_id, route_id):
        return RepositoryImpl.get_route_stop_from_ids_repo_(stop_id, route_id)
    
    def get_trips_from_route_repo(route_id):
        return RepositoryImpl.get_trips_from_route_repo_(route_id)