import unittest

from backend.domain.repositories.user_repository import UserRepository
from backend.tests.mock.user_repository_mock import UserRepositoryMock
from backend.domain.user.get_user import GetUser
from backend.domain.user.user_login import UserLogin

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        user_repo = UserRepository(UserRepositoryMock())
        get_user = GetUser(user_repo)
        self.user_login = UserLogin(get_user)

    def test_do_login_success(self):
        message = self.user_login.do_login('maria@email.com', '12345')
        self.assertEqual(message, {'message' : 'You are logged in'})

    def test_do_login_fail(self):
        message = self.user_login.do_login('maria@email.com', '54321')
        self.assertEqual(message, {'message' : 'Wrong password'})