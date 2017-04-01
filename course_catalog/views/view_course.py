from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session


@app.route('/departments/<int:dept_id>/courses/<course_id>/')  # NOQA
def viewCourse(dept_id, course_id):
    return "View course_id %s of dept_id %s" % (course_id, dept_id)
