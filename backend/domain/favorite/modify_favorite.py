from backend.domain.repositories.favorites_repository import FavoritesRepository
from backend.domain.favorite.favorite import Favorite
from datetime import datetime

class ModifyFavorite:

    def create_favorite_(email, route_id, stop_id):
        new_favorite = Favorite(email, route_id, stop_id)
        FavoritesRepository.add_new_favorite(new_favorite)
        return {'message' : 'success: favorite created'}

    def delete_favorite_(email, route_id, stop_id, time):
        time_ = datetime.strptime(time, '%H:%M:%S').time()
        favorite = Favorite(email, route_id, stop_id, None, time_)
        FavoritesRepository.remove_favorite(favorite)
        return {'message' : 'success: favorite deleted'}        