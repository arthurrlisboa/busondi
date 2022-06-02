from backend.domain.repositories.favorites_repository import FavoritesRepository
from backend.domain.favorite.favorite import Favorite

class GetFavorite:

    def get_all_user_favorites(email):
        all_user_favorites = FavoritesRepository.get_all_user_favorites_repo(email)
        favorites_list = []
        for favorite in all_user_favorites:
            favorites_list.append(Favorite(favorite.email, favorite.route_id, favorite.stop_id, favorite.favorite_id, favorite.time))
        return favorites_list  