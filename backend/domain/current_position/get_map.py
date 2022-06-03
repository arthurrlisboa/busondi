from backend.domain.current_position.get_map_impl import GetMapImpl

class GetMap:
    
    def get_actual_map(route_id):
        return GetMapImpl.get_actual_map_impl(route_id)