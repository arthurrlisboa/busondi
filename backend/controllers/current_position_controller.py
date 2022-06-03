from backend.domain.current_position.get_map import GetMap
from flask import jsonify

def current_position_map(route_id):
    map = GetMap.get_actual_map(route_id)
    print(map)
    return jsonify({'message':'success'})