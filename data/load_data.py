from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.database.models.bus_departures import BusDepartures
from backend.database.models.route_stop import RouteStop
from backend.database.models.shapes import Shapes
from backend.database.models.bus_stops import BusStops
from backend.database.models.routes import Routes

import csv
#import geopandas as gpd
from shapely import wkt
from datetime import datetime


engine = create_engine('sqlite:///./backend/database.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def load_bus_stops(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ',')
        for row in csv_reader:
            bus_stops = BusStops(stop_id=row['stop_id'], stop_name=row['stop_name'],
                                    stop_lat=row['stop_lat'], stop_lon=row['stop_lon'])
            session.add(bus_stops)
            session.commit()


def load_shapes(filename):
    shape_file = gpd.read_file(filename)
    shape_file['str_polygon'] = shape_file.geometry.apply(lambda x: wkt.dumps(x))
    for idx, row in shape_file.iterrows():
        shapes = Shapes(shape_id=row['shape_id'], polygon=row['str_polygon'])
        session.add(shapes)
        session.commit()


def load_routes(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ',')
        for row in csv_reader:
            routes = Routes(route_id=row['route_id'], route_short_name=row['route_short_name'],
                            route_long_name=row['route_long_name'], shape_id=row['shape_id'],
                            initial_stop_id=row['initial_stop_id'], final_stop_id=row['final_stop_id'])
            session.add(routes)
            session.commit()


def load_bus_departures(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ',')
        for row in csv_reader:
            time_obj = datetime.strptime(row['departure_time'], '%H:%M:%S').time()
            bus_departures = BusDepartures(trip_id=row['trip_id'], departure_time=time_obj,
                            stop_id=row['stop_id'], route_id=row['route_id'])
            session.add(bus_departures)
            session.commit()


def load_route_stop(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ',')
        for row in csv_reader:
            route_stop = RouteStop(route_stop_id=row['route_stop_id'], route_id=row['route_id'],
                            stop_id=row['stop_id'], stop_sequence=row['stop_sequence'])
            session.add(route_stop)
            session.commit()


path = './data/processed/'

#load_bus_stops(path + 'bus_stops.csv')
#load_shapes(path + 'shapes/shapes.shp')
#load_routes(path + 'routes.csv')
#load_bus_departures(path + 'bus_departures.csv')
#load_route_stop(path + 'route_stop.csv')
