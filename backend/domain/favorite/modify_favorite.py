from backend.domain.favorite.modify_favorite_impl import ModifyFavoriteImpl

class ModifyFavorite:

    def __init__(self):
        self.impl = ModifyFavoriteImpl()

    def new_favorite(self, email, route_id, stop_id):
        return self.impl.new_favorite_impl(email, route_id, stop_id)

    def exclude_favorite(self, email, route_id, stop_id, time):
        return self.impl.exclude_favorite_impl(email, route_id, stop_id, time)