from backend.adapters.user_repository_impl import UserRepositoryImpl

class UserRepository:

    def get_all_users_repo():
        return UserRepositoryImpl.get_all_users_repo_()

    def add_new_user(user):
        UserRepositoryImpl.add_new_user_(user)

    def get_user_by_email_repo(email):
        return UserRepositoryImpl.get_user_by_email_repo_(email)

    def update_user_password_repo(email, new_password):
        UserRepositoryImpl.update_user_password_repo_(email, new_password)

    def delete_user_repo(email):
        UserRepositoryImpl.delete_user_repo_(email)