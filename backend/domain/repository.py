from backend.repository_impl import RepositoryImpl

class Repository:
    def get_all_stops_repo():
        return RepositoryImpl.get_all_stops_repo_()

    def get_stop_by_id_repo(stop_id):
        return RepositoryImpl.get_stop_by_id_repo_(stop_id)

    def get_routes_from_stop_repo(stop_id):
        return RepositoryImpl.get_routes_from_stop_repo_(stop_id)