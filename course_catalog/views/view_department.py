from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc
from sqlalchemy.exc import DBAPIError, SQLAlchemyError


@app.route('/departments/<int:dept_id>/')
@app.route('/departments/<int:dept_id>/courses/')
def viewDepartment(dept_id):
    # retrieve given dept from DB
    try:
        departments = session.query(Department).order_by(asc(Department.name))
        curr_dept = session.query(Department).filter_by(id=dept_id).one()
        courses = session.query(Course).filter_by(department_id=dept_id)
    # handle database exceptions
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404, requested URL was not found! Exception occured in Database."
    else:
        return render_template("dept_page.html", departments=departments,
                               curr_dept=curr_dept, courses=courses)
