from backend.domain.favorite.modify_favorite_impl import ModifyFavoriteImpl

class ModifyFavorite:

    def create_favorite_port(email, route_id, stop_id):
        return ModifyFavoriteImpl.create_favorite_(email, route_id, stop_id)

    def delete_favorite_port(email, route_id, stop_id, time):
        return ModifyFavoriteImpl.delete_favorite_(email, route_id, stop_id, time)