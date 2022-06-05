from domain.user.get_user import GetUser

class UserLoginImpl:

    def do_login_impl(email, password):
        user = GetUser.get_user_by_email(email)
        if user.password == password:
            return {'message' : 'You are logged in'}
        else:
            return {'message' : 'Wrong password'}