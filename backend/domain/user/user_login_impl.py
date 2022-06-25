from backend.domain.user.get_user import GetUser

class UserLoginImpl:

    def __init__(self, get_user=None):
        if(get_user is None):
            self.get_user = GetUserImpl()
        else:
            self.get_user = get_user

    def do_login_impl(self, email, password):
        user = self.get_user.get_user_by_email_impl(email)
        if user.password == password:
            return {'message' : 'You are logged in'}
        else:
            return {'message' : 'Wrong password'}