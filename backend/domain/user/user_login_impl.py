from backend.domain.user.get_user import GetUserImpl

class UserLoginImpl:

    def do_login_impl(email, password):
        user = GetUserImpl().get_user_by_email_impl(email)
        if user.password == password:
            return {'message' : 'You are logged in'}
        else:
            return {'message' : 'Wrong password'}