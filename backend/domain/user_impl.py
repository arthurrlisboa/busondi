from backend.domain.repository import Repository

class UserImpl:
    email = ''
    password = ''

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def get_all_users():
        all_users = Repository.get_all_users_repo()
        user_list = []
        for user in all_users:
            user_list.append(UserImpl(user.email, user.password))
        return user_list

    def create_user_(email, password):
        new_user = UserImpl(email, password)
        Repository.add_new_user(new_user)
        return {'success' : 'user created'}