from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc


@app.route('/departments/<int:dept_id>/')
@app.route('/departments/<int:dept_id>/courses/')
def viewDepartment(dept_id):
    departments = session.query(Department).order_by(asc(Department.name))
    curr_dept = session.query(Department).filter_by(id=dept_id).one()
    return render_template("dept_page.html", departments=departments,
                           curr_dept=curr_dept)
