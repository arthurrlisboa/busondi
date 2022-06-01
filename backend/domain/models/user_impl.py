from backend.domain.repositories.user_repository import UserRepository

class UserImpl:
    email = ''
    password = ''
    name = ''

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def get_all_users():
        all_users = UserRepository.get_all_users_repo()
        user_list = []
        for user in all_users:
            user_list.append(UserImpl(user.email, user.password, user.name))
        return user_list

    def create_user_(email, password, name):
        new_user = UserImpl(email, password, name)
        UserRepository.add_new_user(new_user)
        return {'success' : 'user created'}

    def get_user_by_email(email):
        user_repo = UserRepository.get_user_by_email_repo(email)
        user = UserImpl(user_repo.email, user_repo.password, user_repo.name)
        return user

    def update_user_password(email, new_password):
        UserRepository.update_user_password_repo(email, new_password)

    def delete_user_(email):
        UserRepository.delete_user_repo(email)
        return {'success' : 'user deleted'}