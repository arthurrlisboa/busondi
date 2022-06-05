from domain.repositories.user_repository import UserRepository
from domain.user.user import User

class GetUserImpl:

    def get_all_users_impl():
        all_users = UserRepository.return_all_users()
        user_list = []
        for user in all_users:
            user_list.append(User(user.email, user.password, user.name))
        return user_list

    def get_user_by_email_impl(email):
        user_repo = UserRepository.return_one_user_by_email(email)
        user = User(user_repo.email, user_repo.password, user_repo.name)
        return user