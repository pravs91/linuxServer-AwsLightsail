from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc


@app.route('/departments/<int:dept_id>/courses/<course_id>/')  # NOQA
def viewCourse(dept_id, course_id):
    departments = session.query(Department).order_by(asc(Department.name))
    curr_dept = session.query(Department).filter_by(id=dept_id).one()
    dept_courses = session.query(Course).filter_by(department_id=dept_id)
    curr_course = session.query(Course).filter_by(id=course_id).one()
    return render_template("course_page.html", departments=departments,
                           curr_dept=curr_dept, dept_courses=dept_courses,
                           curr_course=curr_course)
