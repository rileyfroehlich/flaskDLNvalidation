from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from form import dlnvForm

app = Flask(__name__)
app.config.from_object(__name__)
# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'Ftcc9uACqVnPPuuK5EtsUvguUwYIyi0P'


@app.route("/dlnv")
def validate():
    form = dlnvForm()
    return render_template('dlnpage.html', title='Validator', form=form)


if __name__ == '__main__':
    app.run(debug=True)