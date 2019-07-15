from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

ROLES = [('client', 'Client'),('admin','Admin'),('dev','Dev')]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    Submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    email = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    FirstName = StringField('Username', validators=[DataRequired()])
    LastName = StringField('Username', validators=[DataRequired()])
    Role = SelectField('Roles', choices=ROLES, default=1)
    Submit = SubmitField('Sign In')