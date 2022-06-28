import unittest

from backend.domain.repositories.user_repository import UserRepository
from backend.tests.mock.user_repository_mock import UserRepositoryMock
from backend.domain.user.get_user import GetUser

class TestGetUser(unittest.TestCase):
    def setUp(self):
        user_repo = UserRepository(UserRepositoryMock())
        self.get_user = GetUser(user_repo)

    def test_get_all_users(self):
        users_list = self.get_user.get_all_users()
        self.assertEqual(users_list[0].__dict__, {
            'email': 'maria@email.com', 
            'password': '12345', 
            'name': 'Maria'})
        self.assertEqual(users_list[1].__dict__, {
            'email': 'joao@email.com', 
            'password': '12345', 
            'name': 'Joao'})
        self.assertEqual(users_list[2].__dict__, {
            'email': 'laura@email.com', 
            'password': '12345', 
            'name': 'Laura'})

    def test_get_user_by_email(self):
        user = self.get_user.get_user_by_email('maria@email.com')
        self.assertEqual(user.__dict__, {
            'email': 'maria@email.com', 
            'password': '12345', 
            'name': 'Maria'})