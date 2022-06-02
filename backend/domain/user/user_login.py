from backend.domain.user.user_login_impl import UserLoginImpl

class UserLogin:
    def do_login_port(email, password):
        return UserLoginImpl.do_login(email, password)