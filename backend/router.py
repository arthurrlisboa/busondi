from backend import controller
from backend.app import app

@app.route('/')
def home():
   return controller.home()

@app.route('/stops/', methods = ['GET'])
def stops():
   return controller.list_stops()

@app.route('/stops/<stop_id>/', methods = ['GET'])
def stops_stop_id(stop_id):
   return controller.list_routes_from_stop(stop_id)