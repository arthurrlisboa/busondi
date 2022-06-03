from backend.domain.current_position.get_bus_coords_impl import GetBusCoordsImpl

class GetBusCoords:
    
    def get_bus_coords(route_id):
        return GetBusCoordsImpl.get_bus_coords_impl(route_id)