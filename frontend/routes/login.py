
from .. import app

from flask import Flask, render_template, request, redirect, flash, url_for

from flask_login import current_user, login_required, LoginManager, login_user
from ..forms import LoginForm, RegisterForm
from sqlalchemy import select

from flask_login import login_user
from ..db import User, Session
from datetime import *


login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


users = []
passwords = []

@login_manager.user_loader
def load_user(user_id):
    with Session.begin() as session:
        user = session.scalar(select(User).where(User.id == user_id))
        if user:
            user = User(email=user.email)
            return user
    

@app.get('/register')
def register():
    form = RegisterForm()
    return render_template('form_template.html', form=form)

@app.post('/register')
def register_post():
    form = RegisterForm()
    if form.validate_on_submit():
       with Session.begin() as session:
           user = session.scalar(select(User).where(User.email == form.email.data))
           if user:
               flash("User exists!")
               return redirect(url_for('register'))
           pwd = form.password.data
           user = User(
               nickname = form.email.data.split('@')[0],
               email = form.email.data,
               password = pwd,
               # ДАТА СОЗДАНИЯ АККАУНТА ТУТ 
           )
           session.add(user)
           users.append(user.nickname)
           passwords.append(user.password)