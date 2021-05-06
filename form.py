from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

#This is the form that populates the webpage '/' and '/submission'
class dlnvForm(FlaskForm):
    #name info
    fName = StringField('What is your First Name?', validators=[DataRequired(), Length(min=1)])
    mName = StringField('What is your Middle Name?', validators=[Optional()])
    lName = StringField('What is your Last Name?', validators=[DataRequired(), Length(min=1)])
    #personal info
    month = StringField('What is your birth month? (i.e. January)', validators=[DataRequired(), Length(min=3)])
    day = StringField('What is your day of birth?', validators=[DataRequired(), Length(min=1,max=2)])
    year = StringField('What is your birth year? (i.e. 1978)', validators=[DataRequired(), Length(min=4,max=4)])
    sex = StringField('What is the registered sex on your Drivers License? (i.e. M or F)', validators=[DataRequired(), Length(min=1)])
    eyeColor = StringField('What is the eye color printed on your Drivers License? (i.e. Hazel)', validators=[DataRequired(), Length(min=1)])
    #DL info
    dlNumber = StringField('What is your Drivers License Number?', validators=[DataRequired(), Length(min=1)])
    issueDay = StringField('What day was your Drivers License issued? (i.e. 1)', validators=[DataRequired(), Length(min=1,max=2)])
    issueMonth = StringField('What month was your Drivers License issued? (i.e. January)', validators=[DataRequired(), Length(min=3)])
    issueYear = StringField('What year was your Drivers License issued? (i.e. 1978)', validators=[DataRequired(), Length(min=4,max=4)])
    dlDay = StringField('What day does your Drivers License Expire? (i.e. 1)', validators=[DataRequired(), Length(min=1,max=2)])
    dlMonth = StringField('What month does your Drivers License Expire? (i.e. January)', validators=[DataRequired(), Length(min=3)])
    dlYear = StringField('What year does your Drivers License Expire? (i.e. 1978)', validators=[DataRequired(), Length(min=4,max=4)])
    state = StringField('What is your DL State Code (i.e. CA, TX)?', validators=[DataRequired(), Length(min=2)])
    #submit button
    submit = SubmitField('Submit Validation Check')