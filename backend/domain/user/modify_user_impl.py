from backend.domain.user.user import User

class ModifyUserImpl:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def new_user_impl(self, email, password, name):
        new_user = User(email, password, name)
        self.user_repo.add_user(new_user)
        return {'message' : 'User created'}

    def update_user_password_impl(self, email, new_password):
        self.user_repo.change_user_password(email, new_password)

    def exclude_user_impl(self, email):
        self.user_repo.remove_user(email)
        return {'message' : 'User deleted'}   