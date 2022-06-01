from backend.database.config.db_connection import DBConnection
from backend.database.models.favorites import Favorites

class FavoritesRepositoryImpl:
    def get_all_user_favorites_repo_(email):
        with DBConnection() as connection:
            favorites = connection.session.query(Favorites).filter_by(email=email).all()
        return favorites

    def add_new_favorite_(favorite):
        id = FavoritesRepositoryImpl.generate_new_favorite_id()
        new_favorite = Favorites(id, favorite.email, favorite.route_id, favorite.stop_id)
        with DBConnection() as connection:
            connection.session.add(new_favorite)
            connection.session.commit()

    def generate_new_favorite_id():
        with DBConnection() as connection:
            all_favorites = connection.session.query(Favorites).all()
        if all_favorites == []:
            return 0
        return all_favorites[-1].favorite_id + 1

    def remove_favorite_(favorite):
        with DBConnection() as connection:
            found_favorite = connection.session.query(Favorites).filter_by(email=favorite.email, route_id=favorite.route_id, stop_id=favorite.stop_id, time=favorite.time).first()
            connection.session.delete(found_favorite)
            connection.session.commit()