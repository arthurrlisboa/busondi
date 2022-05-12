import backend.controller
from backend.app import app

@app.route('/')
def home():
   return backend.controller.home()

@app.route('/stops/', methods = ['GET'])
def stops():
   return backend.controller.stops()

@app.route('/stops/<stop_id>/', methods = ['GET'])
def stops_stop_id(stop_id):
   return backend.controller.stop_id(stop_id)