##from backend.database.config import init_database
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#init_database.init_database()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

busondi_database = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()

import backend.router