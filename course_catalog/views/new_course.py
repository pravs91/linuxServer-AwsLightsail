from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session


@app.route('/departments/<int:dept_id>/courses/new/', methods=['GET', 'POST'])
def newCourse(dept_id):
    return "Create a new course under dept_id %s" % dept_id
