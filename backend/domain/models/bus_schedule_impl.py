from backend.domain.repositories.routes_repository import RoutesRepository

import datetime

MEAN_BUS_VELOCITY = 5  # velocity in m/s

def get_travel_time_timedelta(stop_id, route_id):
    route_stop = RoutesRepository.get_route_stop_from_ids_repo(stop_id, route_id)
    if not route_stop.traveled_time: 
        travel_time = route_stop.traveled_dist / MEAN_BUS_VELOCITY
    else:
        travel_time = route_stop.traveled_time
    return datetime.timedelta(seconds=round(travel_time,2))

def get_current_time_timedelta():
    cur_datetime = datetime.datetime.now()
    return datetime.timedelta(hours=cur_datetime.hour, 
                            minutes=cur_datetime.minute, 
                            seconds=round(cur_datetime.second,2))

def get_timedelta_from_time_obj(time_obj):
    return datetime.timedelta(hours=time_obj.hour, 
                            minutes=time_obj.minute, 
                            seconds=round(time_obj.second,2))

def get_arrival_time(stop_id, route_id):
    travel_time_timedelta = get_travel_time_timedelta(stop_id, route_id)

    trip_list = RoutesRepository.get_trips_from_route_repo(route_id)
    current_time = get_current_time_timedelta()
    best_arrival_time = None
    for trip in trip_list:
        time_obj = trip.departure_time
        departure_time = get_timedelta_from_time_obj(time_obj)
        arrival_time = departure_time + travel_time_timedelta
        if (arrival_time > current_time and (not best_arrival_time or arrival_time < best_arrival_time)):
            best_arrival_time = arrival_time
            
    return (str(best_arrival_time) or '')