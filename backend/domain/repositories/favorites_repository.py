from backend.adapters.favorites_repository_impl import FavoritesRepositoryImpl

class FavoritesRepository:
    def get_all_user_favorites_repo(email):
        return FavoritesRepositoryImpl.get_all_user_favorites_repo_(email)

    def add_new_favorite(favorite):
        FavoritesRepositoryImpl.add_new_favorite_(favorite)

    def remove_favorite(favorite):
        FavoritesRepositoryImpl.remove_favorite_(favorite)