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


@app.route("/", methods = ['GET', 'POST'])
def validate():
    form = dlnvForm()
    if form.validate_on_submit():
 #       if {validation} is not False:
            return redirect(url_for('submit'))
    return render_template('dlnpage.html', title='Validator', form=form)

@app.route("/submission", methods = ['GET','POST'])
def submit():
    fName = request.form['fName']
    mName = request.form['mName']
    lName = request.form['lName']
    dlNumber = request.form['dlNumber']
    state = request.form['state']
    month = request.form['month']
    day = request.form['day']
    year = request.form['year']
    sex = request.form['sex']
    dlDay = request.form['dlDay']
    dlMonth = request.form['dlMonth']
    dlYear = request.form['dlYear']
    form = dlnvForm()

    response = check_is_valid(state, dlNumber, fName, lName, mName, month, day, year, sex, dlDay, dlMonth, dlYear)
    if response == True:
        flash(f"Your Driver's License Number is Valid", 'success')
    else:
        flash(response, 'danger')
    return render_template('dlnpage.html', title='Validator', form=form)