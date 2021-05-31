# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, url_for, flash
from tripdata import car, trip
from forms import TripDataForm
import os


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY=os.environ.get('ML_APPKEY')
))


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
            flash('Täytä kaikki kentät. Tiedot kokonaislukuina!')
    return render_template('index.html', form=form, result=result, data=data)


def main():
    app.run(debug=True)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
