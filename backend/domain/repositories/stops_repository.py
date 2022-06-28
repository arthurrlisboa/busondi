from backend.adapters.stops_repository_impl import StopsRepositoryImpl

class StopsRepository:

    def __init__(self, repo=None):
        if(repo is None):
            self.repo = StopsRepositoryImpl()
        else:
            self.repo = repo
    
    def return_all_stops(self):
        return self.repo.return_all_stops_impl()

    def return_stop_by_id(self, stop_id):
        return self.repo.return_stop_by_id_impl(stop_id)

    def return_all_stops_in_list(self, stops_list):
        return self.repo.return_all_stops_in_list_impl(stops_list)