import unittest

from backend.domain.repositories.user_repository import UserRepository
from backend.tests.mock.user_repository_mock import UserRepositoryMock
from backend.domain.user.modify_user import ModifyUser

class TestModifyUser(unittest.TestCase):
    def setUp(self):
        user_repo = UserRepository(UserRepositoryMock())
        self.modify_user = ModifyUser(user_repo)

    def test_new_user(self):
        message = self.modify_user.new_user('maria@email.com', '12345', 'Maria')
        self.assertEqual(message, {'message' : 'User created'})

    def test_update_user_password(self):
        message = self.modify_user.update_user_password('maria@email.com', '54321')
        self.assertEqual(message, {'message' : 'Password updated'})

    def test_exclude_user(self):
        message = self.modify_user.exclude_user('maria@email.com')
        self.assertEqual(message, {'message' : 'User deleted'})