from backend.domain.favorite.get_favorite_impl import GetFavoriteImpl
from backend.domain.repositories.favorites_repository import FavoritesRepository

class GetFavorite:

    def __init__(self, favorites_repo=None):
        if(favorites_repo is None):
            self.impl = GetFavoriteImpl(FavoritesRepository())
        else:
            self.impl = GetFavoriteImpl(favorites_repo)

    def get_all_user_favorites(self, email):
        return self.impl.get_all_user_favorites_impl(email)