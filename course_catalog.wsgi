#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/course_catalog/")

activate_this = '/var/www/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

from course_catalog import app as application
application.secret_key = 'mankal_and_buj'
