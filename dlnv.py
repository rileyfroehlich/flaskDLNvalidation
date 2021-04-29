from flask import Flask, render_template, redirect, url_for, request
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


@app.route("/")
def validate():
    form = dlnvForm()
    if form.validate_on_submit():
 #       if {validation} is not False:
            flash(f"Your Drivers License Number is {validation}!")
            return redirect(url_for('submit'))
    return render_template('dlnpage.html', title='Validator', form=form)

@app.route("/submission", methods = ['POST'])
def submit():
    fName = request.form['fName']
    lName = request.form['lName']
    dlNumber = request.form['dlNumber']
    state = request.form['state']
    form = dlnvForm()

    print( check_is_valid(state, dlNumber))

    if form.validate_on_submit():
#       if {validation} is not False:
            flash(f"Your Drivers License Number is {validation}!")
            return redirect(url_for('submit'))
    return render_template('dlnpage.html', title='Validator', form=form)

if __name__ == '__main__':
    app.run(debug=True)