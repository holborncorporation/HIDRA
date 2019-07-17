from flask import Flask, redirect, render_template, session, flash, url_for
from allForms import *
from config import Config
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
            info = get_companies()
            flash('Signed in as: ' + session['username'], "sign")
            return render_template("home.html", data=info)
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
            flash('Signed in as: ' + session['username'], "sign")
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
    print("logout")
    # remove the username from the session if it is there
    session.pop('userId', None)
    session.pop('username', None)
    session.pop('name', None)
    return redirect(url_for('login'))


def check_user():
    if 'userId' in session:
        print("Check User: " + session['userId'])
        result = find_user_id(session['userId'])
        if result:
            flash('Signed in as: ' + session['username'], "sign")
            return True
        else:
            return False
    else:
        return False


@app.route('/addcompany', methods=['GET', 'POST'])
def addcompany():
    form = AddCompanyForm();
    check = check_user()
    if check:
        try:
            if form.validate_on_submit():
                user_info = add_compnay(form.CompanyName.data, form.Logo.data)
                print(user_info)
                session.pop('_flashes', None)
                if user_info:
                    flash("Company Added", "success")
                    return redirect(url_for('addcompany'))
                else:
                    flash("An error occurred!", "error")
            else:
                print(form.errors)
                return render_template('company.html', form=form)
        except Exception as e:
            flash(e)
        return render_template('company.html', form=form)
    else:
        return redirect("login")


if __name__ == '__main__':
    app.run(debug=True)
