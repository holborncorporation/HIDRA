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
    print("Home")
    if 'username' in session:
        print("Home")
        print(session['username'])
        #       We should check to make sure the username is legit through the db before allowing user forward
        flash('Welcome, ' + session['name'])
        return render_template("home.html")
    else:
        print("Redirect")
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        print(session['username'])
#       We should check to make sure the username is legit through the db before allowing user forward
        flash('Welcome,' + session['name'])
        return redirect(url_for("home"))
    form = LoginForm()
    try:
        if form.validate_on_submit():
            print("inside Validate")
            print(form.username.data)
            user_info = find_user(form.username.data, form.password.data)
            print(user_info)
            if user_info:
                session.pop('_flashes', None)
                session['username'] = user_info.get('email')
                session['name'] = user_info.get('firstName')
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
            print("inside Validate")
            print(form.email.data)
            print(form.FirstName.data)
            print(form.LastName.data)
            print(form.password.data)
            print(form.Role.data)

            user_info = add_user(form.email.data, form.FirstName.data, form.LastName.data, form.password.data,
                                 form.Role.data)
            print(user_info)
            if user_info:
                flash("Registered")
                return redirect(url_for('home'))
        else:
            print(form.errors)
            return render_template('register.html', form=form)
    except Exception as e:
        flash(e)

    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
