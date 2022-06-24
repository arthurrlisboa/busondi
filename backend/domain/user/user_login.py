from backend.domain.user.user_login_impl import UserLoginImpl

class UserLogin:
    
    def do_login(email, password):
        return UserLoginImpl().do_login_impl(email, password)