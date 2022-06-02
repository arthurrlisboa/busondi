from backend.domain.favorite.modify_favorite import ModifyFavorite
from backend.domain.favorite.get_favorite import GetFavorite
from flask import jsonify, render_template

def list_user_favorites(email):
    user_favorites = GetFavorite.get_all_user_favorites_port(email)
    favorites_dict = {}
    for favorite in user_favorites:
        favorites_dict[favorite.id] = {
            'route_id' : favorite.route_id,
            'stop_id' : favorite.stop_id,
            'time' : str(favorite.time)
        }
    return render_template("list_user_favorites.html", user_favorites=jsonify(favorites_dict))

def create_favorite(email, route_id, stop_id):
    response = ModifyFavorite.create_favorite_port(email, route_id, stop_id)
    return jsonify(response)

def delete_favorite(email, route_id, stop_id, time):
    response = ModifyFavorite.delete_favorite_port(email, route_id, stop_id, time)
    return jsonify(response)