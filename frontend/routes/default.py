from os import getenv
from flask_login import current_user, login_required
from flask import render_template
from requests import get
from .. import app

BACKEND_URL = getenv("BACKEND_URL")

@app.get("/")
@login_required
def index():
    email = current_user.email
    data = {
        "email": email
    }
    tasks = {
        "tasks": get(f"{BACKEND_URL}/default", json=data).json() 
    }
    return render_template("index.html", **tasks)