from backend.database.config.db_connection import DBConnection
from backend.database.models.favorites import Favorites

class FavoritesRepositoryImpl:

    def __init__(self):
        self.conn = DBConnection()

    def return_all_user_favorites_impl(self, email):
        with self.conn as connection:
            favorites = connection.session.query(Favorites).filter_by(email=email).all()
        return favorites

    def add_favorite_impl(self, favorite):
        id = FavoritesRepositoryImpl().generate_new_favorite_id()
        new_favorite = Favorites(id, favorite.email, favorite.route_id, favorite.stop_id)
        with self.conn as connection:
            connection.session.add(new_favorite)
            connection.session.commit()

    def generate_new_favorite_id(self):
        with self.conn as connection:
            all_favorites = connection.session.query(Favorites).all()
        if all_favorites == []:
            return 0
        return all_favorites[-1].favorite_id + 1

    def remove_favorite_impl(self, favorite):
        with self.conn as connection:
            found_favorite = connection.session.query(Favorites).filter_by(email=favorite.email, route_id=favorite.route_id, stop_id=favorite.stop_id, time=favorite.time).first()
            connection.session.delete(found_favorite)
            connection.session.commit()