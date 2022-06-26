from backend.domain.favorite.modify_favorite_impl import ModifyFavoriteImpl
from backend.domain.repositories.favorites_repository import FavoritesRepository

class ModifyFavorite:

    def __init__(self, favorites_repo=None):
        if(favorites_repo is None):
            self.impl = ModifyFavoriteImpl(FavoritesRepository())
        else:
            self.impl = ModifyFavoriteImpl(favorites_repo)

    def new_favorite(self, email, route_id, stop_id):
        return self.impl.new_favorite_impl(email, route_id, stop_id)

    def exclude_favorite(self, email, route_id, stop_id, time):
        return self.impl.exclude_favorite_impl(email, route_id, stop_id, time)