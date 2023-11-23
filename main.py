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
    """All the cafes in the db are queried and organized in a list with a vector of
    3 cafes each, so it can be displayed this way using jinjer"""
    cafes_query = Cafe.query.all()
    cafes_dict = [cafe.to_dict() for cafe in cafes_query]
    cafes_ordered = []
    for i in range(0, len(cafes_query), 3):
        cafes_ordered.append(cafes_dict[i:i+3])

    print(cafes_ordered)

    return render_template("index.html", all_cafes=cafes_ordered)


@app.route('/cafe/<int:cafe_id>', methods=['POST', 'GET'])
def cafe_details(cafe_id):
    requested_cafe = db.get_or_404(Cafe, cafe_id)

    return render_template('cafe.html', cafe=requested_cafe)


@app.route('/about')
def about():
    pass


if __name__ == '__main__':
    app.run(debug=True)
