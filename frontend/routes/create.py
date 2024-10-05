from os import getenv
from flask import render_template, request, redirect, url_for
from flask_login import current_user
from requests import post
from .. import app


BACKEND_URL=getenv("BACKEND_URL")
@app.get('/create')
def create():
    return render_template('create.html')


@app.post('/create')
def create_book():
    author = current_user.email
    content = request.form.get("content")
    data = {'author' : author, 'content' : content}
    response = post(f"{BACKEND_URL}/create", json=data)
    if response.status_code==200:
        return redirect(url_for('index'))
