from backend.database.config.db_connection import DBConnection
from backend.database.models.user import User

class UserRepositoryImpl:

    def return_all_users_impl():
        with DBConnection() as connection:
            all_users = connection.session.query(User).all()
        return all_users

    def add_user_impl(user):
        new_user = User(user.email, user.password, user.name)
        with DBConnection() as connection:
            connection.session.add(new_user)
            connection.session.commit()

    def return_one_user_by_email_impl(email):
        with DBConnection() as connection:
            user = connection.session.query(User).get(email)
        return user

    def change_user_password_impl(email, new_password):
        with DBConnection() as connection:
            user = connection.session.query(User).get(email)
            user.set_password(new_password)
            connection.session.commit()

    def remove_user_impl(email):
        with DBConnection() as connection:
            user = connection.session.query(User).get(email)
            connection.session.delete(user)
            connection.session.commit()