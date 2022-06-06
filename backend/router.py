from backend.controllers import user_controller, route_controller, bus_stop_controller, favorite_controller
from flask import jsonify, request, session, make_response
from backend.app import app
from flask_cors import cross_origin

# Home
@app.route('/')
def home():
   return make_response(jsonify({'message' : 'Home'}), 200)

# Stop
@app.route('/stops', methods = ['GET'])
@cross_origin()
def stops():
   return bus_stop_controller.list_stops()

@app.route('/stops/<stop_id>', methods = ['GET'])
@cross_origin()
def stops_stop_id(stop_id):
   return route_controller.return_stop_and_routes(stop_id)

# User
@app.route('/users', methods = ['GET', 'POST'])
@cross_origin()
def users():
   if request.method == 'GET':
      return user_controller.list_users()
   if request.method == 'POST':
      info_json = request.get_json()
      return user_controller.create_user(info_json)

@app.route('/users/<email>', methods = ['GET', 'PUT', 'DELETE'])
@cross_origin()
def users_user_id(email):
   if request.method == 'GET':
      return user_controller.return_user(email)
   if request.method == 'PUT':
      info_json = request.get_json()
      return user_controller.update_user(email, info_json)
   if request.method == 'DELETE':
      return user_controller.delete_user(email)

# Login/logout
@app.route('/login', methods = ['POST'])
@cross_origin()
def login():
   info_json = request.get_json()
   return user_controller.user_login(info_json)

@app.route('/logout', methods = ['POST'])
@cross_origin()
def logout():
   return user_controller.user_logout()

# Favorites
@app.route('/favorites', methods = ['GET', 'POST', 'DELETE'])
@cross_origin()
def favorites():
   if 'email' in session:   
      if request.method == 'GET':
         return favorite_controller.list_user_favorites(session['email'])
      if request.method == 'POST':
         info_json = request.get_json()
         return favorite_controller.create_favorite(session['email'], info_json)
      if request.method == 'DELETE':
         info_json = request.get_json()
         return favorite_controller.delete_favorite(session['email'], info_json)
   else:
      return make_response(jsonify({'message' : 'Login required'}), 401)

# Routes
@app.route('/routes', methods = ['GET'])
@cross_origin()
def routes():
   return route_controller.list_routes()

@app.route('/routes/<route_id>', methods = ['GET'])
@cross_origin()
def routes_route_id(route_id):
   return route_controller.return_route_and_stops(route_id)

@app.route('/routes/<route_id>/current-position', methods = ['GET'])
@cross_origin()
def routes_route_id_current_position(route_id):
   return route_controller.current_position_map(route_id)