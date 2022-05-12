from backend.database.models.bus_stops import BusStops
from backend.app import busondi_database, app

def get_stops():
    all_stops = BusStops.query.all()
    stops_dict = {}
    for stop in all_stops:
        stops_dict[stop.stop_id] = {
            'stop_lat' : stop.stop_lat,
            'stop_lon': stop.stop_lon,
            'stop_name' : stop.stop_name
        }
    return stops_dict