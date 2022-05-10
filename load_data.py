from asyncore import read
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.database.models.shapes import Shapes
from backend.database.models.bus_stops import BusStops
from backend.database.models.routes import Routes

import csv
import codecs


engine = create_engine('sqlite:///./backend/database.db', echo=True)
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
    with open(filename, 'r', encoding='ISO-8859-1') as file:
        #reader = codecs.getreader('utf-8')(file)
        for line in file.readlines():
            print(line.encode('UTF-8'))
        #csv_reader = csv.reader(file)
        #for row in csv_reader:
            #print(row)
            #shapes = Shapes(shape_id=row['shape_id'], polygon=row['polygon'])
            #session.add(shapes)
            #session.commit()


def load_routes(filename):
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ',')
        for row in csv_reader:
            routes = Routes(route_id=row['route_id'], route_short_name=row['route_short_name'],
                            route_long_name=row['route_long_name'], shape_id=row['shape_id'],
                            initial_stop_id=row['initial_stop_id'], final_stop_id=row['final_stop_id'])
            session.add(routes)
            session.commit()


path = './data/processed/'

#load_bus_stops(path + 'bus_stops.csv')

load_shapes(path + 'shapes/shapes.shp')
#load_routes(path + 'routes.csv')