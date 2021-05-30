# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request, redirect, url_for
from tripdata import car, trip
from forms import TripDataForm


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="POJKH876y8756kjHGihg675hjg(/&"
))

@app.route("/", methods=['GET', 'POST'])
def index():
    form = TripDataForm()
    if form.validate_on_submit():
        return redirect('/results')
    print('Not')
    return render_template('index.html', form=form)

@app.route("/results", methods=['GET','POST'])
def results():
    trp1 = trip(form.dist, form.speed1, car(form.car))
    trp2 = trip(request.args.get('dist'), request.args.get('speed2'), car(request.args.get('car')))
    form.car.data = trp1.car.model
    form.dist.data = trp1.dist
    form.speed1.data = trp1.speed
    form.speed2.data = trp2.speed
    return render_template('results.html', data=[trp1, trp2], form=form)

@app.route("/error", methods=['GET','POST'])
def error():
    form = TripDataForm()
    return render_template('error_st.html', form=form)

@app.route("/test")
def test():
    form = TripDataForm()
    return render_template('test.html', form=form)

def main():
    app.run(debug=True)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
