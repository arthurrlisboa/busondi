from flask import Flask
from backend.database.config.init_database import init_database

app = Flask(__name__)
app.config["DEBUG"] = True

init_database()