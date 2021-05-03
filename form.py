from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class dlnvForm(FlaskForm):
    fName = StringField('What is your First Name?', validators=[DataRequired(), Length(min=1)])
    mName = StringField('What is your Middle Name?', validators=[Optional()])
    lName = StringField('What is your Last Name?', validators=[DataRequired(), Length(min=1)])
    month = StringField('What is your birth month? (i.e. January)', validators=[DataRequired(), Length(min=3)])
    day = StringField('What is your day of birth?', validators=[DataRequired(), Length(min=1,max=2)])
    year = StringField('What is your birth year? (i.e. 1978)', validators=[DataRequired(), Length(min=4,max=4)])
    sex = StringField('What is the registered sex on your Drivers License? (i.e. M or F)', validators=[DataRequired(), Length(min=1)])
    dlNumber = StringField('What is your Drivers License Number?', validators=[DataRequired(), Length(min=1)])
    dlDay = StringField('What day does your Drivers License Expire? (i.e. 1)', validators=[DataRequired(), Length(min=1,max=2)])
    dlMonth = StringField('What month does your Drivers License Expire? (i.e. January)', validators=[DataRequired(), Length(min=3)])
    dlYear = StringField('What year does your Drivers License Expire? (i.e. 1978)', validators=[DataRequired(), Length(min=4,max=4)])
    state = StringField('What is your DL State Code (i.e. CA, TX)?', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField('Submit Validation Check')