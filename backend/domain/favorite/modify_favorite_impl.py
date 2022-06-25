from backend.domain.favorite.favorite import Favorite
from datetime import datetime

class ModifyFavoriteImpl:

    def __init__(self, favorites_repo):
        self.favorites_repo = favorites_repo

    def new_favorite_impl(self, email, route_id, stop_id):
        new_favorite = Favorite(email, route_id, stop_id)
        self.favorites_repo.add_favorite(new_favorite)
        return {'message' : 'success: favorite created'}

    def exclude_favorite_impl(self, email, route_id, stop_id, time):
        time_ = datetime.strptime(time, '%H:%M:%S').time()
        favorite = Favorite(email, route_id, stop_id, None, time_)
        self.favorites_repo.remove_favorite(favorite)
        return {'message' : 'success: favorite deleted'}        