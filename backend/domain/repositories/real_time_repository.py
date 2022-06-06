from backend.adapters.real_time_repository_impl import RealTimeRepositoryImpl

class RealTimeRepository:

    def get_real_time_bus_coords(route_number):
        return RealTimeRepositoryImpl.get_real_time_bus_coords_impl(route_number)