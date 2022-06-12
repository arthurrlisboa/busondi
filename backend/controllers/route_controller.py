from backend.domain.route_stop.get_route_stop import GetRouteStop
from backend.domain.route.get_bus_coords import GetBusCoords
from backend.domain.route.bus_schedule import BusSchedule
from backend.domain.bus_stop.get_stop import GetStop
from backend.domain.route.get_route import GetRoute
from backend.domain.shape.get_shape import GetShape
from backend.domain.route.draw_map import DrawMap
from flask import jsonify, make_response

def return_stop_and_routes(stop_id):
    try:
        stop = GetStop.get_stop_by_id(stop_id)
    except:
        return make_response(jsonify({'message': 'Stop id not found'}), 404)

    routes_list = GetRoute.get_routes_from_stop(stop_id)
    routes_dict = {
        'stop_routes' : []
    }

    for entry in routes_list:
        arrival_time = BusSchedule.get_arrival_time(stop_id, entry[1].route_id)
        if arrival_time != 'None':
            routes_dict['stop_routes'].append({
                'route_id' : entry[1].route_id,
                'route_name' : entry[1].route_short_name, 
                'time' : arrival_time})
    #routes_dict['stop_routes'] = BusSchedule.order_by_arrival_time(routes_dict['stop_routes'])

    return make_response(jsonify(routes_dict), 200)

def current_position_map(route_id):
    try:
        polygon = GetShape.get_polygon(route_id)
        bus_coords = GetBusCoords.get_bus_coords(route_id)
        bus_stops_coords = GetRouteStop.get_coordinates_stops_in_route(route_id)
    except:
        return make_response(jsonify({'message' : 'Route id not found'}), 404)
    map = DrawMap.draw_map_route_stops_bus_position(polygon, bus_coords, bus_stops_coords)
    return make_response(map, 200)

def list_routes():
    routes_list = GetRoute.get_all_routes()

    # routes_dict = {}
    # for route in routes_list:
    #     routes_dict[route.route_id] = {
    #         'route_short_name' : route.route_short_name,
    #         'route_long_name': route.route_long_name
    #     }

    routes_new_list = [{
        'route_id': route.route_id,
        'route_short_name' : route.route_short_name,
        'route_long_name': route.route_long_name
    } for route in routes_list]

    return routes_new_list

def return_route_and_stops(route_id):
    try:
        route = GetRoute.get_route_by_id(route_id)

        stops_list = GetStop.get_stops_from_route(route_id)
    except:
        return make_response(jsonify({'message': 'Route id not found'}), 404)

    """
    stops_list_ = []
    for stop in stops_list:
        stops_list_.append({stop.stop_id : stop.stop_name})

    return make_response(jsonify({'stops' : stops_list_}), 200)
    """

    new_stops_list = [{
        'stop_id': stop.stop_id,
        'stop_lat' : stop.stop_lat,
        'stop_lon': stop.stop_lon,
        'stop_name' : stop.stop_name
    } for stop in stops_list]

    route_stops_dict = {
        'route_id' : route.route_id,
        'route_short_name' : route.route_short_name,
        'route_long_name' : route.route_long_name,
        'stops' : new_stops_list
    }

    return route_stops_dict
