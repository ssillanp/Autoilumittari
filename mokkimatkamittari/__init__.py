from flask import Flask
from boto.s3.connection import S3Connection
import os


app = Flask(__name__)
app.config['SECRET_KEY']=S3Connection(os.environ['ML_APPKEY'], os.environ['ML_APPKEY'])

from mokkimatkamittari import routes