from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from flask import session as login_session
from sqlalchemy import asc

import random
import string
from gplus_login import gdisconnect
from fb_login import fbdisconnect


@app.route('/')
@app.route('/departments/')
def showDepartments():
    departments = session.query(Department).order_by(asc(Department.name))
    return render_template("dept_page.html", departments=departments,
                           curr_dept=departments[0])


@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/logout')
def logout():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showDepartments'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showDepartments'))
