from backend.domain.favorite.modify_favorite import ModifyFavorite
from backend.domain.favorite.get_favorite import GetFavorite
from flask import jsonify, make_response

def list_user_favorites(email):
    user_favorites = GetFavorite.get_all_user_favorites(email)
    favorites_dict = {
        'user_favorites' : user_favorites
    }
    return make_response(jsonify(favorites_dict), 200)

def create_favorite(email, info_json):
    if 'route_id' in info_json and 'stop_id' in info_json:
        if info_json['route_id'] and info_json['stop_id']:
            response = ModifyFavorite.new_favorite(email, info_json['route_id'], info_json['stop_id'])
            return make_response(jsonify(response), 200)
    return make_response(jsonify({'message' : 'Invalid credentials - route_id and stop_id fields required'}), 400)
            

def delete_favorite(email, info_json):
    if 'route_id' in info_json and 'stop_id' in info_json and 'time' in info_json:
        if info_json['route_id'] and info_json['stop_id'] and info_json['time']:
            try:
                response = ModifyFavorite.exclude_favorite(email, info_json['route_id'], 
                                                           info_json['stop_id'], 
                                                           info_json['time'])
                return jsonify(response)
            except:
                return make_response(jsonify({'message' : 'Favorite not found'}), 404)
    return make_response(jsonify({'message' : 'Invalid credentials - route_id, stop_id and time fields required'}), 400)