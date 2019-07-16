from flask import Flask, redirect, render_template, session, flash, url_for
from config import Config
import logging
# from flask_login import *
from loginform import *
from models import *


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
@app.route('/home')
def home():
    if 'userId' in session:
        print(session['userId'])
        result = find_user_id(session['userId'])
        if result:
            flash('Signed in as: ' + session['username'])
            return render_template("home.html")
        else:
            session.pop('userId', None)
            session.pop('username', None)
            session.pop('name', None)
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'userId' in session:
        result = find_user_id(session['userId'])
        if result:
            flash('Signed in as: ' + session['username'])
            return render_template("home.html")
    form = LoginForm()
    try:
        if form.validate_on_submit():
            print("inside Validate")
            user_info = find_user(form.username.data, form.password.data)
            print(user_info)
            if user_info:
                session.pop('_flashes', None)
                session['userId'] = str(user_info.get('_id'))
                session['username'] = user_info.get('email')
                session['name'] = user_info.get('firstName')
                session.permanent = True
                return redirect(url_for('home'))
        else:
            print(form.errors)
            return render_template('login.html', form=form)
    except Exception as e:
        flash(e)

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm();
    try:
        if form.validate_on_submit():
            user_info = add_user(form.email.data, form.FirstName.data, form.LastName.data, form.password.data,
                                 form.Role.data)
            print(user_info)
            session.pop('_flashes', None)
            if user_info:
                flash("Registered")
                return redirect(url_for('home'))
            else:
                flash("An error occurred! User already exists")
        else:
            print(form.errors)
            return render_template('register.html', form=form)
    except Exception as e:
        flash(e)

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
    session.pop('userId', None)
    session.pop('username', None)
    session.pop('name', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
