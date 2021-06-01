from flask import render_template, flash, url_for
from mokkimatkamittari import app
from mokkimatkamittari.tripdata import car, trip
from mokkimatkamittari.forms import TripDataForm


@app.route("/", methods=['GET', 'POST'])
def index():
    result = False
    data = None
    form = TripDataForm()
    if form.validate_on_submit():
        trp1 = trip(form.dist.data, form.speed1.data, car(form.car.data))
        trp2 = trip(form.dist.data, form.speed2.data, car(form.car.data))

        data = [trp1, trp2]
        result = True
    else:
        if form.is_submitted():
            for key, value in form.errors.items():
                flash(value[0])
    return render_template('index.html', form=form, result=result, data=data)