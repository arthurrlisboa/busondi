from backend.repository_impl import RepositoryImpl

class Repository:
    #Stops
    def get_all_stops_repo():
        return RepositoryImpl.get_all_stops_repo_()

    def get_stop_by_id_repo(stop_id):
        return RepositoryImpl.get_stop_by_id_repo_(stop_id)

    # Routes
    def get_routes_from_stop_repo(stop_id):
        return RepositoryImpl.get_routes_from_stop_repo_(stop_id)

    # Users
    def get_all_users_repo():
        return RepositoryImpl.get_all_users_repo_()

    def add_new_user(user):
        RepositoryImpl.add_new_user_(user)

    def get_user_by_email_repo(email):
        return RepositoryImpl.get_user_by_email_repo_(email)

    def update_user_password_repo(email, new_password):
        RepositoryImpl.update_user_password_repo_(email, new_password)

    def delete_user_repo(email):
        RepositoryImpl.delete_user_repo_(email)