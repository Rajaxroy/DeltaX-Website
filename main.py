from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

from flask_wtf.file import FileField, FileAllowed, FileRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string' 
Bootstrap(app)

class MyForm(FlaskForm):
    name = StringField('Name ', validators=[DataRequired()])
    date = StringField("Date Released eg: 'July 17, 2019' ", validators=[DataRequired()])
    upload = FileField('Upload image ', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    artist = SelectField('Artist ', choices=["Arijit", "Sidhu Mosewala","Guru"])
    submit = SubmitField("Save ")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add", methods=['GET', 'POST'])
def add_song():
    form = MyForm()
    return render_template("add.html", form=form)

@app.route("/all-songs")
def all_songs():
    return render_template("allSongs.html")

@app.route("/all-artist")
def all_artists():
    return render_template("allArtists.html")


if __name__ == "__main__":
    app.run(debug=True)