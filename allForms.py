from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired

ROLES = [('client', 'Client'),('admin','Admin'),('dev','Dev')]


class AddCompanyForm(FlaskForm):
    CompanyName = StringField('Company Name', validators=[DataRequired()])
    Logo = FileField('Upload', validators=[FileRequired()])
