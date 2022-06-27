import unittest
from backend.app import app

class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        app.testing = True
        self.app = app.test_client()
        self.app_context = app.app_context
        self.app_context().push()