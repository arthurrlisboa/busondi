from backend.domain.repositories.user_repository import UserRepository
from backend.domain.user.user import User

class ModifyUserImpl:

    def create_user_(email, password, name):
        new_user = User(email, password, name)
        UserRepository.add_new_user(new_user)
        return {'message' : 'user created'}

    def update_user_password(email, new_password):
        UserRepository.update_user_password_repo(email, new_password)

    def delete_user_(email):
        UserRepository.delete_user_repo(email)
        return {'message' : 'user deleted'}