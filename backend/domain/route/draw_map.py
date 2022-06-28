from backend.domain.route.draw_map_impl import DrawMapImpl

class DrawMap:
    
    def draw_map_route_stops_bus_position(polygon, bus_coord, stops_coord):
        return DrawMapImpl.draw_map_route_stops_bus_position_impl(polygon, bus_coord, stops_coord)