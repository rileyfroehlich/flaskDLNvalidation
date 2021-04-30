from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class dlnvForm(FlaskForm):
    fName = StringField('What is your First Name?', validators=[DataRequired(), Length(min=1)])
    lName = StringField('What is your Last Name?', validators=[DataRequired(), Length(min=1)])
    month = StringField('What is your birth month? (i.e. January)', validators=[DataRequired(), Length(min=1)])
    day = StringField('What is your day of birth?', validators=[DataRequired(), Length(min=1)])
    year = StringField('What is your birth year? (i.e. 1978)', validators=[DataRequired(), Length(min=1)])
    sex = StringField('What is the registered sex on your Drivers License? (i.e. M or F)', validators=[DataRequired(), Length(min=1)])
    dlNumber = StringField('What is your Drivers License Number?', validators=[DataRequired(), Length(min=1)])
    state = StringField('What is your DL State Code (i.e. CA, TX)?', validators=[DataRequired(), Length(min=1)])
    submit = SubmitField('Submit Validation Check')