from backend.domain.favorite.get_favorite_impl import GetFavoriteImpl

class GetFavorite:

    def __init__(self):
        self.impl = GetFavoriteImpl()

    def get_all_user_favorites(self, email):
        return self.impl.get_all_user_favorites_impl(email)