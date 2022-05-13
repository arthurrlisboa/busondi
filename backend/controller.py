from flask import render_template
from backend.context import stops_py, routes_py


def home():
    return render_template("home.html")

def list_stops():
    stops_json = stops_py.get_all_stops()
    return render_template("stops.html", stops=stops_json)

def list_routes_from_stop(stop_id):
    routes_json = routes_py.get_routes_from_stop(stop_id)
    return render_template("stops_id.html", routes=routes_json)