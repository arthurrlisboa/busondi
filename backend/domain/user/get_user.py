from domain.user.get_user_impl import GetUserImpl

class GetUser:
    def get_all_users():
        return GetUserImpl.get_all_users_impl()

    def get_user_by_email(email):
        return GetUserImpl.get_user_by_email_impl(email)