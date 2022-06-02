from backend.domain.repositories.user_repository import UserRepository
from backend.domain.user.user import User

class GetUserImpl:

    def get_all_users():
        all_users = UserRepository.get_all_users_repo()
        user_list = []
        for user in all_users:
            user_list.append(User(user.email, user.password, user.name))
        return user_list

    def get_user_by_email(email):
        user_repo = UserRepository.get_user_by_email_repo(email)
        user = User(user_repo.email, user_repo.password, user_repo.name)
        return user