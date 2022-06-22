from backend.domain.user.modify_user_impl import ModifyUserImpl

class ModifyUser:

    def __init__(self):
        self.impl = ModifyUserImpl()

    def new_user(self, email, password, name):
        return self.impl.new_user_impl(email, password, name)

    def update_user_password(self, email, new_password):
        self.impl.update_user_password_impl(email, new_password)

    def exclude_user(self, email):
        return self.impl.exclude_user_impl(email)