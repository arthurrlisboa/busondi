from backend.domain.user.get_user import GetUser

class UserLogin:

    def do_login(email, password):
        user = GetUser.get_user_by_email(email)
        if user:
            if user.password == password:
                return {'message' : 'You are logged in'}
            else:
                return {'message' : 'Wrong password'}
        else:
            return {'message' : 'User does not exist'}