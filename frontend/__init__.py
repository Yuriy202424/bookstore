from flask import Flask
from os import getenv

SECRET_KEY = getenv("SECRET_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


from . import routes