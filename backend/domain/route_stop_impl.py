from backend.domain.repository import Repository

import datetime

MEAN_BUS_VELOCITY = 5  # velocity in m/s

def get_next_trip_time(route_id, travel_time):
        trip_list = Repository.get_trips_from_route_repo(route_id)
        time_obj = trip_list[0].departure_time
        departure_time = datetime.timedelta(hours=time_obj.hour, minutes=time_obj.minute, seconds=round(time_obj.second,2))
        arrival_time = departure_time + datetime.timedelta(seconds=round(travel_time,2))
        return str(arrival_time)

def get_arrival_time(stop_id, route_id):
        route_stop = Repository.get_route_stop_from_ids_repo(stop_id, route_id)
        if not route_stop.traveled_time: 
            travel_time = route_stop.traveled_dist / MEAN_BUS_VELOCITY
        else:
            travel_time = route_stop.traveled_time
        return get_next_trip_time(route_id, travel_time)