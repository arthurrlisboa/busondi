from domain.favorite.get_favorite_impl import GetFavoriteImpl

class GetFavorite:
    def get_all_user_favorites(email):
        return GetFavoriteImpl.get_all_user_favorites_impl(email)