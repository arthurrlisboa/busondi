from flask import render_template
from context.stops_py import get_stops
from context.routes_py import get_routes


def home():
    return render_template("home.html")

def stops():
    stops_json = get_stops()
    return render_template("stops.html", stops=stops_json)

def stop_id(id):
    routes_json = get_routes(id)
    return render_template("stops_id.html", routes=routes_json)