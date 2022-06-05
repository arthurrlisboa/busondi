from adapters.user_repository_impl import UserRepositoryImpl

class UserRepository:

    def return_all_users():
        return UserRepositoryImpl.return_all_users_impl()

    def add_user(user):
        UserRepositoryImpl.add_user_impl(user)

    def return_one_user_by_email(email):
        return UserRepositoryImpl.return_one_user_by_email_impl(email)

    def change_user_password(email, new_password):
        UserRepositoryImpl.change_user_password_impl(email, new_password)

    def remove_user(email):
        UserRepositoryImpl.remove_user_impl(email)