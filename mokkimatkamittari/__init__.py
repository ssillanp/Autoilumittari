from flask import Flask
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = "c25071b35496070b34a024ad6c0cf43ab0ee4174654ccb76845897afe5d8b396"

from mokkimatkamittari import routes