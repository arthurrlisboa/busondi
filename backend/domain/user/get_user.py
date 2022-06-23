from backend.domain.user.get_user_impl import GetUserImpl

class GetUser:

    def __init__(self):
        self.impl = GetUserImpl()

    def get_all_users(self):
        return self.impl.get_all_users_impl()

    def get_user_by_email(self, email):
        return self.impl.get_user_by_email_impl(email)