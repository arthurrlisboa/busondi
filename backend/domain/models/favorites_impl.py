from backend.domain.repositories.favorites_repository import FavoritesRepository
from datetime import datetime

class FavoriteImpl:
    id = ''
    email = ''
    route_id = ''
    stop_id = ''
    time = ''

    def __init__(self, email, route_id, stop_id, id=None, time=None):
        self.email = email
        self.route_id = route_id
        self.stop_id = stop_id

        if(id is None):
            self.id = ''
        else:
            self.id = id

        if(time is None):
            self.time = ''
        else:
            self.time = time       

    def get_all_user_favorites(email):
        all_user_favorites = FavoritesRepository.get_all_user_favorites_repo(email)
        favorites_list = []
        for favorite in all_user_favorites:
            favorites_list.append(FavoriteImpl(favorite.email, favorite.route_id, favorite.stop_id, favorite.favorite_id, favorite.time))
        return favorites_list

    def create_favorite_(email, route_id, stop_id):
        new_favorite = FavoriteImpl(email, route_id, stop_id)
        FavoritesRepository.add_new_favorite(new_favorite)
        return {'message' : 'success: favorite created'}

    def delete_favorite_(email, route_id, stop_id, time):
        time_ = datetime.strptime(time, '%H:%M:%S').time()
        favorite = FavoriteImpl(email, route_id, stop_id, None, time_)
        FavoritesRepository.remove_favorite(favorite)
        return {'message' : 'success: favorite deleted'}        