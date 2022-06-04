from backend.domain.bus_stop.get_stop import GetStop
from backend.domain.repositories.favorites_repository import FavoritesRepository
from backend.domain.route.get_route import GetRoute

class GetFavoriteImpl:

    def get_all_user_favorites_impl(email):
        all_user_favorites = FavoritesRepository.return_all_user_favorites(email)
        favorites_dict = {}
        for favorite in all_user_favorites:
            route_name = GetRoute.get_route_by_id(favorite.route_id).route_short_name
            stop_name = GetStop.get_stop_by_id(favorite.stop_id).stop_name
            favorites_dict[favorite.favorite_id] = {
                'route_id' : favorite.route_id,
                'route_short_name' : route_name,
                'stop_id' : favorite.stop_id,
                'stop_name' : stop_name,
                'time' : str(favorite.time)
            }
        return favorites_dict