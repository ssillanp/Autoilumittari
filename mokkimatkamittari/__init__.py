from flask import Flask
from boto.s3.connection import S3Connection
import os


app = Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('ML_APPKEY')

from mokkimatkamittari import routes