from backend.domain.user.get_user_impl import GetUserImpl

class GetUser:
    def get_all_users_port():
        return GetUserImpl.get_all_users()

    def get_user_by_email_port(email):
        return GetUserImpl.get_user_by_email(email)