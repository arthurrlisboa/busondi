import imp
import unittest

from backend.domain.repositories.user_repository import UserRepository
from backend.tests.mock.user_repository_mock import UserRepositoryMock
from backend.domain.user.get_user_impl import GetUserImpl
from backend.domain.user.user_login_impl import UserLoginImpl

class TestUserLoginImpl(unittest.TestCase):
    def setUp(self):
        user_repo = UserRepository(UserRepositoryMock())
        get_user = GetUserImpl(user_repo)
        self.user_login = UserLoginImpl(get_user)

    def test_do_login_impl_success(self):
        message = self.user_login.do_login_impl('maria@email.com', '12345')
        self.assertEqual(message, {'message' : 'You are logged in'})

    def test_do_login_impl_fail(self):
        message = self.user_login.do_login_impl('maria@email.com', '54321')
        self.assertEqual(message, {'message' : 'Wrong password'})