from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session


@app.route('/departments/<int:dept_id>/')
@app.route('/departments/<int:dept_id>/courses/')
def viewDepartment(dept_id):
    return "This handler is to view courses of dept_id %s" % dept_id
