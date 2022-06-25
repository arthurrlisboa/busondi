from backend.domain.user.modify_user_impl import ModifyUserImpl
from backend.domain.repositories.user_repository import UserRepository

class ModifyUser:

    def __init__(self, user_repo=None):
        if(user_repo is None):
            self.impl = ModifyUserImpl(UserRepository())
        else:
            self.impl = ModifyUserImpl(user_repo)

    def new_user(self, email, password, name):
        return self.impl.new_user_impl(email, password, name)

    def update_user_password(self, email, new_password):
        self.impl.update_user_password_impl(email, new_password)

    def exclude_user(self, email):
        return self.impl.exclude_user_impl(email)