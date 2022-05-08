from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String

db_user = SQLAlchemy()

class User(db_user.Model):

    __tablename__ = 'user'

    email = Column(String, primary_key=True)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = password