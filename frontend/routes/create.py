from os import getenv
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from requests import post
from .. import app


BACKEND_URL = getenv("BACKEND_URL")
@app.get('/create')
@login_required
def create():
    return render_template('create.html')


@app.post('/create')
@login_required
def create_task():
    author = current_user.email
    content = request.form.get("content")
    data = {'author' : author, 'content' : content}
    print("*" * 80)
    print(data)
    response = post(f"{BACKEND_URL}/create", json=data)
    if response.status_code==200:
        return redirect(url_for('index'))
    else: 
        code = response.status_code
        text = response.text
        return render_template("errors.html", code=code, text=text)