# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request
from tripdata import car, trip

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/results")
def results():
    trp = trip(request.args.get('dist'), request.args.get('speed'), car(request.args.get('car')))
    h, m, s = trp.trip_duration()
    return f"Matka kestää {h}h {m}min {s}s ja polttoainetta kuluu {trp.trip_consumption()} litraa."




def main():
    app.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
