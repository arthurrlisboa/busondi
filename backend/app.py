from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'busondi-session-key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

busondi_database = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()

import backend.router