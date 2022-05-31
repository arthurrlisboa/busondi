from backend.database.config.db_connection import DBConnection
from backend.database.models.user import User

class UserRepositoryImpl:

    def get_all_users_repo_():
        with DBConnection() as connection:
            all_users = connection.session.query(User).all()
        return all_users

    def add_new_user_(user):
        new_user = User(user.email, user.password, user.name)
        with DBConnection() as connection:
            connection.session.add(new_user)
            connection.session.commit()

    def get_user_by_email_repo_(email):
        with DBConnection() as connection:
            user = connection.session.query(User).get(email)
        return user

    def update_user_password_repo_(email, new_password):
        with DBConnection() as connection:
            user = connection.session.query(User).get(email)
            user.set_password(new_password)
            connection.session.commit()

    def delete_user_repo_(email):
        with DBConnection() as connection:
            user = connection.session.query(User).get(email)
            connection.session.delete(user)
            connection.session.commit()