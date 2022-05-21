'''
Esse script somente funciona se executado no diretório raiz do projeto
'''

from backend.database.config.db_connection import DBConnection
from backend.database.models.bus_stops import BusStops
from backend.database.models.route_stop import RouteStop
from backend.database.models.routes import Routes
import sqlite3

import openrouteservice
import haversine as hs
from haversine import Unit


'''
Chave de acesso à API obtida em: https://openrouteservice.org 
'''
client = openrouteservice.Client(key='5b3ce3597851110001cf62481fa455a3a0bf46c284d1d66aa9352574')


def get_distance_api(coords):
  res = client.directions(coords)
  try: 
    return(res['routes'][0]['summary']['distance'], res['routes'][0]['summary']['duration'])
  except:
    return 0,0


def get_distance_func(coords):
  departure, arrival = coords
  return(hs.haversine(departure, arrival, unit=Unit.METERS))


def update_route_stop_table_api(route_stop_id, dist, time):
  db = sqlite3.connect('backend/database.db')
  c = db.cursor()
  c.execute(""" UPDATE route_stop 
            SET traveled_dist=?, traveled_time=?
            WHERE route_stop.route_stop_id=? """, (dist, time, route_stop_id))
  db.commit()


def update_route_stop_table_hs(route_stop_id, dist):
  db = sqlite3.connect('backend/database.db')
  c = db.cursor()
  c.execute(""" UPDATE route_stop 
            SET traveled_dist=?
            WHERE route_stop.route_stop_id=? """, (dist, route_stop_id))
  db.commit()


def update_route_stop_from_route_id(route_id):
  with DBConnection() as connection:
      route_stops = connection.session.query(RouteStop).filter_by(route_id=route_id).all()
      for route_stop in route_stops:
        stop_id = route_stop.stop_id
        bus_stop = connection.session.query(BusStops).filter_by(stop_id=stop_id).first()
        if route_stop.stop_sequence == 1: 
          departure_lat, departure_lon = bus_stop.stop_lat, bus_stop.stop_lon
          total_dist = 0
          #total_time = 0
        arrival_lat, arrival_lon = bus_stop.stop_lat, bus_stop.stop_lon
        #dist, time = get_distance_api(((departure_lon,departure_lat),(arrival_lon, arrival_lat)))
        dist = get_distance_func(((departure_lat, departure_lon),(arrival_lat, arrival_lon)))
        total_dist += dist
        #total_time += time
        #update_route_stop_table_api(route_stop.route_stop_id, total_dist, total_time)
        #update_route_stop_table_hs(route_stop.route_stop_id, round(total_dist,2))
        print('route_id: {}   dist: {}'.format(route_stop.route_stop_id, round(total_dist,2)))
        departure_lat, departure_lon = arrival_lat, arrival_lon


def update_route_stop():
  with DBConnection() as connection:
      routes = connection.session.query(Routes.route_id).all()
      for route in routes:
        route_id = route[0]
        update_route_stop_from_route_id(route_id)


#update_route_stop()
#update_route_stop_from_route_id('2033  01')
#update_route_stop_from_route_id('206   01')