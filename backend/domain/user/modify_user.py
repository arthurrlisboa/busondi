from domain.user.modify_user_impl import ModifyUserImpl

class ModifyUser:

    def new_user(email, password, name):
        return ModifyUserImpl.new_user_impl(email, password, name)

    def update_user_password(email, new_password):
        ModifyUserImpl.update_user_password_impl(email, new_password)

    def exclude_user(email):
        return ModifyUserImpl.exclude_user_impl(email)