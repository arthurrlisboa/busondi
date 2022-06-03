from backend.controllers import user_controller, route_controller, bus_stop_controller, favorite_controller, current_position_controller
from flask import jsonify, render_template, request, session
from backend.app import app

# Home
@app.route('/')
def home():
   return render_template("home.html")

# Stop
@app.route('/stops/', methods = ['GET'])
def stops():
   return bus_stop_controller.list_stops()

@app.route('/stops/<stop_id>/', methods = ['GET'])
def stops_stop_id(stop_id):
   return route_controller.return_stop_and_routes(stop_id)

# User
@app.route('/users/', methods = ['GET', 'POST'])
def users():
   if request.method == 'GET':
      return user_controller.list_users()
   if request.method == 'POST':
      info_json = request.get_json()
      return user_controller.create_user(info_json['email'], info_json['password'], info_json['name'])

@app.route('/users/<email>/', methods = ['GET', 'PUT', 'DELETE'])
def users_user_id(email):
   if request.method == 'GET':
      return user_controller.return_user(email)
   if request.method == 'PUT':
      info_json = request.get_json()
      return user_controller.update_user(email, info_json['password'])
   if request.method == 'DELETE':
      return user_controller.delete_user(email)

# Login/logout
@app.route('/login/', methods = ['POST'])
def login():
   info_json = request.get_json()
   if info_json['email'] and info_json['password']:
      return user_controller.user_login(info_json['email'], info_json['password'])
   else: 
      return jsonify({'message' : 'Invalid credentials'})

@app.route('/logout/', methods = ['POST'])
def logout():
   return user_controller.user_logout()

# Favorites
@app.route('/favorites/', methods = ['GET', 'POST', 'DELETE'])
def favorites():
   if 'email' in session:   
      if request.method == 'GET':
         return favorite_controller.list_user_favorites(session['email'])
      if request.method == 'POST':
         info_json = request.get_json()
         return favorite_controller.create_favorite(session['email'], info_json['route_id'], info_json['stop_id'])
      if request.method == 'DELETE':
         info_json = request.get_json()
         return favorite_controller.delete_favorite(session['email'], info_json['route_id'], info_json['stop_id'], info_json['time'])
   else:
      return jsonify({'message' : 'Login required'})

# Current Position
@app.route('/current-position/<route_id>/', methods = ['GET'])
def current_position(route_id):
   return current_position_controller.current_position_map(route_id)