from backend.domain.bus_stop.get_stop import GetStop
from flask import jsonify, make_response

def list_stops():
    stops_list = GetStop().get_all_stops()

    # stops_dict = {}
    # for stop in stops_list:
    #     stops_dict[stop.stop_id] = {
    #         'stop_id': stop.stop_id,
    #         'stop_lat' : stop.stop_lat,
    #         'stop_lon': stop.stop_lon,
    #         'stop_name' : stop.stop_name
    #     }
    
    new_list = [{
        'stop_id': stop.stop_id,
        'stop_lat' : stop.stop_lat,
        'stop_lon': stop.stop_lon,
        'stop_name' : stop.stop_name
    } for stop in stops_list]
        
    return new_list