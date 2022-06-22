from backend.domain.route.get_bus_coords_impl import GetBusCoordsImpl

class GetBusCoords:

    def __init__(self):
        self.impl = GetBusCoordsImpl()
    
    def get_bus_coords(self, route_id):
        return self.impl.get_bus_coords_impl(route_id)