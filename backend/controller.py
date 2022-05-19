from backend.domain.bus_stops_impl import BusStopsImpl 
from backend.domain.routes_impl import RoutesImpl
from flask import jsonify, render_template

def home():
    return render_template("home.html")

def list_stops():
    stops_list = BusStopsImpl.get_all_stops()

    stops_dict = {}
    for stop in stops_list:
        stops_dict[stop.stop_id] = {
            'stop_lat' : stop.stop_lat,
            'stop_lon': stop.stop_lon,
            'stop_name' : stop.stop_name
        }
        
    return render_template("stops.html", stops=jsonify(stops_dict))

def list_routes_from_stop(stop_id):
    stop = BusStopsImpl.get_stop_by_id(stop_id)
    routes_list = RoutesImpl.get_routes_from_stop(stop_id)

    routes_dict = {
        'stop_id' : stop.stop_id,
        'stop_name' : stop.stop_name,
        'stop_lat' : stop.stop_lat,
        'stop_lon' : stop.stop_lon,
        'stop_routes' : {}
    }

    for entry in routes_list:
        routes_dict['stop_routes'][entry[0]] = entry[1].route_id

    return render_template("stops_id.html", routes=jsonify(routes_dict))