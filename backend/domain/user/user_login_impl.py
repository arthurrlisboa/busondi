class UserLoginImpl:

    def __init__(self, get_user):
        self.get_user = get_user

    def do_login_impl(self, email, password):
        user = self.get_user.get_user_by_email(email)
        if user.password == password:
            return {'message' : 'You are logged in'}
        else:
            return {'message' : 'Wrong password'}