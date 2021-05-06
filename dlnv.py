from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from form import dlnvForm
from main import check_is_valid

app = Flask(__name__)
app.config.from_object(__name__)
# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'Ftcc9uACqVnPPuuK5EtsUvguUwYIyi0P'

#home page routing
@app.route("/", methods = ['GET', 'POST'])
def validate():
    form = dlnvForm()
    if form.validate_on_submit():
            return redirect(url_for('submit'))
    return render_template('dlnpage.html', title='Validator', form=form)

#after submit clicked redirect to submission
@app.route("/submission", methods = ['GET','POST'])
def submit():
    fName = request.form['fName']
    mName = request.form['mName']
    lName = request.form['lName']
    dlNumber = request.form['dlNumber']
    state = request.form['state']
    day = request.form['day']
    month = request.form['month']
    year = request.form['year']
    sex = request.form['sex']
    eyeColor = request.form['eyeColor']
    issueDay = request.form['issueDay']
    issueMonth = request.form['issueMonth']
    issueYear = request.form['issueYear']
    dlDay = request.form['dlDay']
    dlMonth = request.form['dlMonth']
    dlYear = request.form['dlYear']
    form = dlnvForm()

    #call to main.py passing in all fields
    response = check_is_valid(state, dlNumber, fName, lName, mName, month, day, year, sex, eyeColor,
                                issueDay, issueMonth, issueYear, dlDay, dlMonth, dlYear)

    #print response flash at bottom of page
    if response == True:
        flash(f"Your Driver's License Number is Valid", 'success')
    else:
        flash(response, 'danger')
    return render_template('dlnpage.html', title='Validator', form=form)