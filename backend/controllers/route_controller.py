from backend.domain.route.bus_schedule import BusSchedule
from backend.domain.bus_stop.get_stop import GetStop
from backend.domain.route.get_route import GetRoute
from flask import jsonify, render_template

def return_stop_and_routes(stop_id):
    stop = GetStop.get_stop_by_id(stop_id)
    routes_list = GetRoute.get_routes_from_stop(stop_id)

    routes_dict = {
        'stop_id' : stop.stop_id,
        'stop_name' : stop.stop_name,
        'stop_lat' : stop.stop_lat,
        'stop_lon' : stop.stop_lon,
        'stop_routes' : {}
    }

    for entry in routes_list:
        arrival_time = BusSchedule.get_arrival_time(stop_id, entry[1].route_id)
        if arrival_time != 'None':
            routes_dict['stop_routes'][entry[1].route_id] = [entry[1].route_short_name, arrival_time]
    routes_dict['stop_routes'] = BusSchedule.order_by_arrival_time(routes_dict['stop_routes'])

    return render_template("stops_id.html", routes=jsonify(routes_dict))