from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FileField, \
    IntegerField, DateField
from wtforms.validators import DataRequired


class BasicInfoForm(FlaskForm):
    CompanyName = SelectField('Company Name', validators=[DataRequired()])
    Year = StringField('Year', validators=[DataRequired()])
    AnalysisName = StringField('Analysis Name', validators=[DataRequired()])
    LargeCat = StringField('Large CAT', validators=[DataRequired()])
    SmallCat = StringField('Small CAT', validators=[DataRequired()])
    NonCat = StringField('NON CAT', validators=[DataRequired()])
    CatThreshold = IntegerField('Cat Threshold', validators=[DataRequired()])
    NumOfSims = IntegerField('Number of Sims', validators=[DataRequired()])


class AddCompanyForm(FlaskForm):
    CompanyName = StringField('Company Name', validators=[DataRequired()])
    Logo = FileField('Upload', validators=[FileRequired()])
