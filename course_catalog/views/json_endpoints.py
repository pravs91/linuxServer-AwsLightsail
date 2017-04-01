from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session


@app.route('/departments/JSON/')
def allDepartmentsJSON():
    return "JSON for all departments"


@app.route('/courses/JSON/')
def allCoursesJSON():
    return "JSON for all courses"


@app.route('/departments/<int:dept_id>/JSON/')
def departmentJSON(dept_id):
    return "JSON of dept_id %s" % dept_id


@app.route('/departments/<int:dept_id>/courses/JSON/')
def deptCoursesJSON(dept_id):
    return "JSON of courses of dept_id %s" % dept_id


@app.route('/departments/<int:dept_id>/courses/<course_id>/JSON/')
def courseJSON(dept_id, course_id):
    return "JSON for course %s of dept_id %s" % (course_id, dept_id)
