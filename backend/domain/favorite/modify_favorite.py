from domain.favorite.modify_favorite_impl import ModifyFavoriteImpl

class ModifyFavorite:

    def new_favorite(email, route_id, stop_id):
        return ModifyFavoriteImpl.new_favorite_impl(email, route_id, stop_id)

    def exclude_favorite(email, route_id, stop_id, time):
        return ModifyFavoriteImpl.exclude_favorite_impl(email, route_id, stop_id, time)