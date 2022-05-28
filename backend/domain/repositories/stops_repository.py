from backend.adapters.stops_repository_impl import StopsRepositoryImpl

class StopsRepository:
    
    def get_all_stops_repo():
        return StopsRepositoryImpl.get_all_stops_repo_()

    def get_stop_by_id_repo(stop_id):
        return StopsRepositoryImpl.get_stop_by_id_repo_(stop_id)