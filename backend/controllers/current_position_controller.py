from backend.domain.current_position.get_bus_coords import GetBusCoords
from backend.domain.current_position.get_polygon import GetPolygon
from flask import jsonify

def current_position_map(route_id):
    polygon = GetPolygon.get_polygon(route_id)
    bus_coords = GetBusCoords.get_bus_coords(route_id)
    return jsonify({'message':'success'})