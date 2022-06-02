from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.database.models.favorites import Favorites
from backend.database.models.routes import Routes
from backend.database.models.routes_conversion import RoutesConversion
from backend.database.models.route_stop import RouteStop
from backend.database.models.bus_departures import BusDepartures

import sqlite3
import csv

engine = create_engine('sqlite:///./backend/database.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def update_route_id():
    routes = session.query(Routes.route_id).all()
    for route in routes:
        route_id = route.route_id
        new_route_id = '-'.join(route_id.split())
        db = sqlite3.connect('backend/database.db')
        c = db.cursor()
        c.execute(""" UPDATE routes 
            SET route_id=?
            WHERE routes.route_id=? """, (new_route_id, route_id))
        db.commit()

def update_route_id_on_route_stop():
    route_stops = session.query(RouteStop.route_id).all()
    for route_stop in route_stops:
        route_id = route_stop.route_id
        new_route_id = '-'.join(route_id.split())
        db = sqlite3.connect('backend/database.db')
        c = db.cursor()
        c.execute(""" UPDATE route_stop
            SET route_id=?
            WHERE route_stop.route_id=? """, (new_route_id, route_id))
        db.commit()

def update_route_id_on_bus_departures():
    bus_departures = session.query(BusDepartures.route_id).all()
    for bus_departure in bus_departures:
        route_id = bus_departure.route_id
        new_route_id = '-'.join(route_id.split())
        db = sqlite3.connect('backend/database.db')
        c = db.cursor()
        c.execute(""" UPDATE bus_departures
            SET route_id=?
            WHERE bus_departures.route_id=? """, (new_route_id, route_id))
        db.commit()

def update_route_id_on_favorites():
    favorites = session.query(Favorites.route_id).all()
    for favorite in favorites:
        route_id = favorite.route_id
        new_route_id = '-'.join(route_id.split())
        db = sqlite3.connect('backend/database.db')
        c = db.cursor()
        c.execute(""" UPDATE favorites
            SET route_id=?
            WHERE favorites.route_id=? """, (new_route_id, route_id))
        db.commit()

def create_route_conversion_table():
    #RoutesConversion.__table__.create(engine)
    with open('data/processed/routes_conversion.csv', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter = ',')
        for row in csv_reader:
            routes_conversion = RoutesConversion(route_number=row['route_number'], route_id=row['route_id'])
            session.add(routes_conversion)
            session.commit()

#update_route_id()
#update_route_id_on_route_stop()
#update_route_id_on_bus_departures()
#update_route_id_on_favorites()

#create_route_conversion_table()