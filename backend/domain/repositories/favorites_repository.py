from backend.adapters.favorites_repository_impl import FavoritesRepositoryImpl

class FavoritesRepository:
    def return_all_user_favorites(email):
        return FavoritesRepositoryImpl.return_all_user_favorites_impl(email)

    def add_favorite(favorite):
        FavoritesRepositoryImpl.add_favorite_impl(favorite)

    def remove_favorite(favorite):
        FavoritesRepositoryImpl.remove_favorite_impl(favorite)