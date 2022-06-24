from backend.database.models.user import User

class UserRepositoryMock:

    def return_all_users_impl(self):
        return 0

    def add_user_impl(self, user):
        return 0

    def return_one_user_by_email_impl(self, email):
        if(email == 'maria@email.com'):
            return User('maria@email.com', '12345', 'Maria')
        return 'Invalid User'

    def change_user_password_impl(self, email, new_password):
        return 0

    def remove_user_impl(self, email):
        return 0