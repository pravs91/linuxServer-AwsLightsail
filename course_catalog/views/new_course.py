from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc
from flask import session as login_session


@app.route('/departments/<int:dept_id>/courses/new/', methods=['GET', 'POST'])
def newCourse(dept_id):
    if 'username' not in login_session:
        return redirect('/')
    departments = session.query(Department).order_by(asc(Department.name))
    curr_dept = session.query(Department).filter_by(id=dept_id).one()
    if request.method == "POST":
        pass
    else:
        return render_template("new_course.html", departments=departments,
                               curr_dept=curr_dept)
