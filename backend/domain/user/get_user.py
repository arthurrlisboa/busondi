from backend.domain.user.get_user_impl import GetUserImpl
from backend.domain.repositories.user_repository import UserRepository

class GetUser:

    def __init__(self, user_repo=None):
        if(user_repo is None):
            self.impl = GetUserImpl(UserRepository())
        else:
            self.impl = GetUserImpl(user_repo)

    def get_all_users(self):
        return self.impl.get_all_users_impl()

    def get_user_by_email(self, email):
        return self.impl.get_user_by_email_impl(email)