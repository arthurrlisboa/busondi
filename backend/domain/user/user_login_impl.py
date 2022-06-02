from backend.domain.user.get_user import GetUser

class UserLoginImpl:

    def do_login(email, password):
        user = GetUser.get_user_by_email_port(email)
        if user:
            if user.password == password:
                return {'message' : 'You are logged in'}
            else:
                return {'message' : 'Wrong password'}
        else:
            return {'message' : 'User does not exist'}