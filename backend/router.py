from backend import controller
from backend.app import app
from flask import request

@app.route('/')
def home():
   return controller.home()

@app.route('/stops/', methods = ['GET'])
def stops():
   return controller.list_stops()

@app.route('/stops/<stop_id>/', methods = ['GET'])
def stops_stop_id(stop_id):
   return controller.list_routes_from_stop(stop_id)

@app.route('/users/', methods = ['GET', 'POST'])
def users():
   if request.method == 'GET':
      return controller.list_users()
   if request.method == 'POST':
      info_json = request.get_json()
      return controller.create_user(info_json['email'], info_json['password'])

@app.route('/users/<email>/', methods = ['GET', 'PUT', 'DELETE'])
def users_user_id(email):
   if request.method == 'GET':
      return controller.return_user(email)
   if request.method == 'PUT':
      info_json = request.get_json()
      return controller.update_user(email, info_json['password'])
   if request.method == 'DELETE':
      return controller.delete_user(email)