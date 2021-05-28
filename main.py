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
    trp1 = trip(request.args.get('dist'), request.args.get('speed1'), car(request.args.get('car')))
    trp2 = trip(request.args.get('dist'), request.args.get('speed2'), car(request.args.get('car')))
    return render_template('results.html', data=[trp1, trp2])


def main():
    app.run(debug=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
