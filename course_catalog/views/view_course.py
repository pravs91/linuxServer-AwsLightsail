from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc, and_
from sqlalchemy.exc import DBAPIError, SQLAlchemyError


@app.route('/departments/<int:dept_id>/courses/<course_id>/')  # NOQA
def viewCourse(dept_id, course_id):
    # retrieve course for given dept from DB
    try:
        departments = session.query(Department).order_by(asc(Department.name))
        curr_dept = session.query(Department).filter_by(id=dept_id).one()
        dept_courses = session.query(Course).filter_by(department_id=dept_id)
        curr_course = session.query(Course).filter(
            and_(Course.id == course_id, Course.department_id == dept_id)).one()
    # handle database exceptions
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404, requested URL was not found! Exception occured in Database."
    else:
        return render_template("course_page.html", departments=departments,
                               curr_dept=curr_dept, dept_courses=dept_courses,
                               curr_course=curr_course)
