from flask import Flask
import os


app = Flask(__name__)
app.config['SECRET_KEY']="c25071b34496070b34a024ad6c0cf43ab0ee4176654ccb76845897afe5d8b396"

from autoilumittari import routes