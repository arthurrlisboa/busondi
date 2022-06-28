from backend.adapters.favorites_repository_impl import FavoritesRepositoryImpl

class FavoritesRepository:

    def __init__(self, repo=None):
        if(repo is None):
            self.repo = FavoritesRepositoryImpl()
        else:
            self.repo = repo

    def return_all_user_favorites(self, email):
        return self.repo.return_all_user_favorites_impl(email)

    def add_favorite(self, favorite):
        self.repo.add_favorite_impl(favorite)

    def remove_favorite(self, favorite):
        self.repo.remove_favorite_impl(favorite)