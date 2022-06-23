from backend.adapters.user_repository_impl import UserRepositoryImpl

class UserRepository:

    def __init__(self, repo=None):
        if(repo is None):
            self.repo = UserRepositoryImpl()
        else:
            self.repo = repo

    def return_all_users(self):
        return self.repo.return_all_users_impl()

    def add_user(self, user):
        self.repo.add_user_impl(user)

    def return_one_user_by_email(self, email):
        return self.repo.return_one_user_by_email_impl(email)

    def change_user_password(self, email, new_password):
        self.repo.change_user_password_impl(email, new_password)

    def remove_user(self, email):
        self.repo.remove_user_impl(email)