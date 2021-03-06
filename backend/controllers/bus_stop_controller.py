from backend.domain.bus_stop.get_stop import GetStop

def list_stops():
    stops_list = GetStop().get_all_stops()
    
    new_list = [{
        'stop_id': stop.stop_id,
        'stop_lat' : stop.stop_lat,
        'stop_lon': stop.stop_lon,
        'stop_name' : stop.stop_name
    } for stop in stops_list]
        
    return new_list