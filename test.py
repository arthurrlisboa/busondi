from backend.database.config.db_connection import DBConnection
from backend.database.models.bus_stops import BusStops
from backend.database.models.route_stop import RouteStop
from backend.database.models.routes import Routes

import openrouteservice
import json


""" - setup openrouteservice client with api key, you can signup https://openrouteservice.org 
  if you don't have API key. Its totaly free😊
- After signup, you can see your API key available under the dashboard tab.
"""
client = openrouteservice.Client(key='5b3ce3597851110001cf62481fa455a3a0bf46c284d1d66aa9352574')
#set location coordinates in longitude,latitude order
#coords = ((-43.946025,-19.957181),(-43.946344,-19.956891))
#call API

def get_distance(coords):
  res = client.directions(coords)
  #test our response
  try: 
    return(res['routes'][0]['summary']['distance'], res['routes'][0]['summary']['duration'])
  except:
    return 0,0


with DBConnection() as connection:
    routes = connection.session.query(Routes.route_id).all()
    for route in routes:
      route_id = route[0]
      route_stops = connection.session.query(RouteStop).filter_by(route_id=route_id).all()
      num_stops = len(route_stops)
      for route_stop in route_stops:
        stop_id = route_stop.stop_id
        bus_stop = connection.session.query(BusStops).filter_by(stop_id=stop_id).first()
        if route_stop.stop_sequence == 1: 
          departure_lat, departure_lon = bus_stop.stop_lat, bus_stop.stop_lon
          total_dist = 0
          total_time = 0
        arrival_lat, arrival_lon = bus_stop.stop_lat, bus_stop.stop_lon

        dist, time = get_distance(((departure_lon,departure_lat),(arrival_lon, arrival_lat)))
        total_dist += dist
        total_time += time
        print('route_id: {}  sequence: {}  dist: {}   time: {}'.format(route_stop.route_id, 
                                                        route_stop.stop_sequence, 
                                                        round(total_dist,2), 
                                                        round(total_time,2)))
        departure_lat, departure_lon = arrival_lat, arrival_lon


