from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc, and_
from sqlalchemy.exc import DBAPIError, SQLAlchemyError

# Support JSON endpoints for the app


@app.route('/departments/JSON/')
def allDepartmentsJSON():
    # JSON endpoint for all departments in DB
    departments = session.query(Department).order_by(
        asc(Department.name)).all()
    return jsonify(departments=[dept.serialize for dept in departments])


@app.route('/courses/JSON/')
def allCoursesJSON():
    # JSON endpoint for all courses in DB
    courses = session.query(Course).order_by(asc(Course.department_id)).all()
    return jsonify(courses=[course.serialize for course in courses])


@app.route('/departments/<int:dept_id>/JSON/')
def departmentJSON(dept_id):
    # JSON endpoint for a particular department
    try:
        curr_dept = session.query(Department).filter_by(id=dept_id).one()
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404, requested URL was not found! Exception occured in Database."
    else:
        return jsonify(department=curr_dept.serialize)


@app.route('/departments/<int:dept_id>/courses/JSON/')
def deptCoursesJSON(dept_id):
    # JSON endpoint for a particular department's courses
    try:
        curr_dept = session.query(Department).filter_by(id=dept_id).one()
        dept_courses = session.query(Course).filter_by(
            department_id=dept_id).all()
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404, requested URL was not found! Exception occured in Database."
    else:
        return jsonify(department=curr_dept.serialize,
                       courses=[course.serialize for course in dept_courses])


@app.route('/departments/<int:dept_id>/courses/<course_id>/JSON/')
def courseJSON(dept_id, course_id):
    # JSON endpoint for a particular course of a dept
    try:
        curr_course = session.query(Course).filter(
            and_(Course.id == course_id, Course.department_id == dept_id)).one()
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404, requested URL was not found! Exception occured in Database."
    else:
        return jsonify(course=curr_course.serialize)
