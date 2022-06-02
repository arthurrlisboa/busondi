from backend.domain.repositories.favorites_repository import FavoritesRepository
from backend.domain.favorite.favorite import Favorite

class GetFavoriteImpl:

    def get_all_user_favorites_impl(email):
        all_user_favorites = FavoritesRepository.return_all_user_favorites(email)
        favorites_list = []
        for favorite in all_user_favorites:
            favorites_list.append(Favorite(favorite.email, favorite.route_id, favorite.stop_id, favorite.favorite_id, favorite.time))
        return favorites_list  