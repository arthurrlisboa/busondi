from backend.domain.user.modify_user_impl import ModifyUserImpl

class ModifyUser:

    def create_user_port(email, password, name):
        return ModifyUserImpl.create_user_(email, password, name)

    def update_user_password_port(email, new_password):
        ModifyUserImpl.update_user_password(email, new_password)

    def delete_user_port(email):
        return ModifyUserImpl.delete_user_(email)