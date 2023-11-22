from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

from models import Cafe, db


# App Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cafes.db"

db.init_app(app)

# Configure the table
with app.app_context():
    db.create_all()

# all Flask routes below
@app.route("/")
def home():
    cafes_query = Cafe.query.all()
    db_entries = []
    for cafe in cafes_query:
        db_entries.append(cafe.to_dict())
        print(cafe.to_dict())

    return render_template("index.html", all_posts=db_entries)


@app.route('/about')
def about():
    pass


if __name__ == '__main__':
    app.run(debug=True)
