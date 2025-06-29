from os import getenv
from flask import render_template, redirect, url_for
from flask_login import current_user
from requests import post
from .. import app


BACKEND_URL = getenv("BACKEND_URL")


@app.get('/info/<int:task_id>')
def info(task_id):
    email = current_user.email
    data = {'email' : email}
    task = post(f"{BACKEND_URL}/task/{task_id}", json=data)
    if task.status_code==200:
        return redirect(url_for('index'))