from backend.domain.current_position.draw_map import DrawMap
from backend.domain.current_position.get_bus_coords import GetBusCoords
from backend.domain.current_position.get_polygon import GetPolygon
from backend.domain.route_stop.get_route_stop import GetRouteStop
from flask import jsonify, make_response

def current_position_map(route_id):
    polygon = GetPolygon.get_polygon(route_id)
    bus_coords = GetBusCoords.get_bus_coords(route_id)
    bus_stops_coords = GetRouteStop.get_coordinates_stops_in_route(route_id)
    # DRAW MAP USING polygon and bus_coords
    map = DrawMap.draw_map_route_stops_bus_position(polygon, bus_coords, bus_stops_coords)
    return make_response(jsonify({'map' : map}), 200)