from backend.domain.user.user_login_impl import UserLoginImpl
from backend.domain.user.get_user import GetUser

class UserLogin:

    def __init__(self, get_user=None):
        if(get_user is None):
            self.impl = UserLoginImpl(GetUser())
        else:
            self.impl =  UserLoginImpl(get_user)
    
    def do_login(self, email, password):
        return self.impl.do_login_impl(email, password)