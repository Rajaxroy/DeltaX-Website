
from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField,DateField, FileField,TextAreaField
from wtforms.validators import DataRequired
from wtforms import validators



app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string' 
Bootstrap(app)

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    date = DateField("Date Released", validators=[DataRequired()])
    image = SelectField("Image url", validators=[DataRequired()])
    artist = SelectField('Artist', choices=["Arijit", "Sidhu Mosewala","Guru"])
    submit = SubmitField("Save")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=['GET', 'POST'])
def add_song():
    form = MyForm()
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)