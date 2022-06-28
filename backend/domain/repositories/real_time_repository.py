from backend.adapters.real_time_repository_impl import RealTimeRepositoryImpl

class RealTimeRepository:

    def __init__(self, repo=None):
        if(repo is None):
            self.repo = RealTimeRepositoryImpl()
        else:
            self.repo = repo

    def get_real_time_bus_coords(self, route_number):
        return self.repo.get_real_time_bus_coords_impl(route_number)