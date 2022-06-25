from backend.domain.user.user import User

class GetUserImpl:

    def __init__(self, user_repo):
        self.user_repo = user_repo

    def get_all_users_impl(self):
        all_users = self.user_repo.return_all_users()
        user_list = []
        for user in all_users:
            user_list.append(User(user.email, user.password, user.name))
        return user_list

    def get_user_by_email_impl(self, email):
        user_repo = self.user_repo.return_one_user_by_email(email)
        user = User(user_repo.email, user_repo.password, user_repo.name)
        return user