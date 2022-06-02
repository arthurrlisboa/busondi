from backend.domain.repositories.user_repository import UserRepository
from backend.domain.user.user import User

class ModifyUserImpl:

    def new_user_impl(email, password, name):
        new_user = User(email, password, name)
        UserRepository.add_user(new_user)
        return {'message' : 'user created'}

    def update_user_password_impl(email, new_password):
        UserRepository.change_user_password(email, new_password)

    def exclude_user_impl(email):
        UserRepository.remove_user(email)
        return {'message' : 'user deleted'}