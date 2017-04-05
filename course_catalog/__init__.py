from flask import Flask

app = Flask(__name__)
app.secret_key = 'mankal_and_buj'

from models import *
from views import *
