from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField(label="Cafe Name",
                            validators=[DataRequired()])
    location_url = StringField('Cafe Location on Google Maps',
                               validators=[DataRequired(), URL()])
    open_time = StringField(label="Opening time e.g 8AM",
                            validators=[DataRequired()])
    closing_time = StringField(label="Opening time e.g 8AM",
                               validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating",
                                choices=['☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'])
    power_socket = SelectField(label="Power Socket Availability",
                               choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    wifi_strength = SelectField(label="Wi-Fi Strength Rating",
                                choices=['🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'])
    submit = SubmitField(label="Submit")



# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as data:
            new_cafe = (f"\n{form.cafe_name.data},{form.location_url.data},{form.open_time.data},{form.closing_time.data},"
                        f"{form.coffee_rating.data},{form.wifi_strength.data},{form.power_socket.data}")
            data.write(new_cafe)
        print(new_cafe)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template('cafes.html', cafes=list_of_rows)

@app.route('/about')
def about():
    pass

if __name__ == '__main__':
    app.run(debug=True)

