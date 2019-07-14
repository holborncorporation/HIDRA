from flask import Flask, redirect, render_template
# from flask_login import *

app = Flask(__name__)
# login_manager.init_app(app)


@app.route('/')
def home():
   return render_template("login.html")


if __name__ == '__main__':
    app.run()
