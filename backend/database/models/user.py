from sqlalchemy import Column, String

from backend.database.config.db_base import Base


class User(Base):

    __tablename__ = 'user'

    email = Column(String, primary_key=True)
    password = Column(String)
    name = Column(String)

    def __repr__(self):
        return f'User {self.email}'

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

    def set_password(self, password):
        self.password = password
