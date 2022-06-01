from backend import controller
from backend.app import app
from flask import jsonify, request, session

# Home
@app.route('/')
def home():
   return controller.home()

# Stop
@app.route('/stops/', methods = ['GET'])
def stops():
   return controller.list_stops()

@app.route('/stops/<stop_id>/', methods = ['GET'])
def stops_stop_id(stop_id):
   return controller.list_routes_from_stop(stop_id)

# User
@app.route('/users/', methods = ['GET', 'POST'])
def users():
   if request.method == 'GET':
      return controller.list_users()
   if request.method == 'POST':
      info_json = request.get_json()
      return controller.create_user(info_json['email'], info_json['password'], info_json['name'])

@app.route('/users/<email>/', methods = ['GET', 'PUT', 'DELETE'])
def users_user_id(email):
   if request.method == 'GET':
      return controller.return_user(email)
   if request.method == 'PUT':
      info_json = request.get_json()
      return controller.update_user(email, info_json['password'])
   if request.method == 'DELETE':
      return controller.delete_user(email)

# Login/logout
@app.route('/login/', methods = ['POST'])
def login():
   info_json = request.get_json()
   if info_json['email'] and info_json['password']:
      return controller.user_login(info_json['email'], info_json['password'])
   else: 
      return jsonify({'message' : 'Invalid credentials'})

@app.route('/logout/', methods = ['POST'])
def logout():
   if 'email' in session:
      session.pop('email')
   return jsonify({'message' : 'You are logged out'})

# Favorites
@app.route('/favorites/', methods = ['GET', 'POST', 'DELETE'])
def favorites():
   if 'email' in session:   
      if request.method == 'GET':
         return controller.list_user_favorites(session['email'])
      if request.method == 'POST':
         info_json = request.get_json()
         return controller.create_favorite(session['email'], info_json['route_id'], info_json['stop_id'])
      if request.method == 'DELETE':
         info_json = request.get_json()
         return controller.delete_favorite(session['email'], info_json['route_id'], info_json['stop_id'], info_json['time'])
   else:
      return jsonify({'message' : 'Login required'})
