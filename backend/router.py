from flask import Flask
import controller

app = Flask(__name__)

@app.route('/')
def home():
   return controller.home()

@app.route('/stops/', methods = ['GET'])
def stops():
   return controller.stops()

@app.route('/stops/<stop_id>', methods = ['GET'])
def stop_id(id):
   return controller.stop_id(id)