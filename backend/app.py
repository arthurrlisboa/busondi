from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from datetime import timedelta
from backend.controllers import user_controller, route_controller, bus_stop_controller, favorite_controller
from flask import jsonify, request, session, make_response
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'busondi-session-key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)
app.config['JSON_SORT_KEYS'] = False
app.config['CORS_HEADERS'] = 'Content-Type'

busondi_database = SQLAlchemy(app)

########################

# Routes
@app.route('/api/routes', methods = ['GET'])
@cross_origin()
def routes():
   data = route_controller.list_routes()
   return make_response(jsonify(data), 200)

@app.route('/api/routes/<route_id>', methods = ['GET'])
@cross_origin()
def routes_route_id(route_id):
   return route_controller.return_route_and_stops(route_id)

@app.route('/api/routes/<route_id>/current-position', methods = ['GET'])
@cross_origin()
def routes_route_id_current_position(route_id):
   return route_controller.current_position_map(route_id)

# Stop
@app.route('/api/stops', methods = ['GET'])
@cross_origin()
def stops():
   data = bus_stop_controller.list_stops()
   return make_response(jsonify(data), 200)

@app.route('/api/stops/<stop_id>', methods = ['GET'])
@cross_origin()
def stops_stop_id(stop_id):
   return route_controller.return_stop_and_routes(stop_id)

# User
@app.route('/api/users', methods = ['GET', 'POST'])
@cross_origin()
def users():
   if request.method == 'GET':
      return user_controller.list_users()
   if request.method == 'POST':
      info_json = request.get_json()
      return user_controller.create_user(info_json)

@app.route('/api/users/<email>', methods = ['GET', 'PUT', 'DELETE'])
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
@app.route('/api/login', methods = ['POST'])
@cross_origin()
def login():
   info_json = request.get_json()
   return user_controller.user_login(info_json)

@app.route('/api/logout', methods = ['POST'])
@cross_origin()
def logout():
   return user_controller.user_logout()

# Favorites
@app.route('/api/favorites', methods = ['GET', 'POST', 'DELETE'])
@cross_origin()
def favorites():
   #if 'email' in session:   
   #   if request.method == 'GET':
   #      return favorite_controller.list_user_favorites(session['email'])
   #   if request.method == 'POST':
   #      info_json = request.get_json()
   #      return favorite_controller.create_favorite(session['email'], info_json)
   #   if request.method == 'DELETE':
   #      info_json = request.get_json()
   #      return favorite_controller.delete_favorite(session['email'], info_json)
   #else:
   #   return make_response(jsonify({'message' : 'Login required'}), 401) 
   if request.method == 'GET':
      email = request.headers.get('email')
      return favorite_controller.list_user_favorites(email)
   if request.method == 'POST':
      info_json = request.get_json()
      return favorite_controller.create_favorite(info_json['email'], info_json)
   if request.method == 'DELETE':
      info_json = request.get_json()
      return favorite_controller.delete_favorite(info_json['email'], info_json)

########################

if __name__ == '__main__':
    app.run()
