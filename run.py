from flask import Flask
from config import *

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

app.run(debug)