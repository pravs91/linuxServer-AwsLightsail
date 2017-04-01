from flask import Flask

app = Flask(__name__)

import course_catalog.views
