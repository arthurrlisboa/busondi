from flask_sqlalchemy import SQLAlchemy
from backend.app import app
PATH_TEST = "/api"
db = SQLAlchemy(app)
