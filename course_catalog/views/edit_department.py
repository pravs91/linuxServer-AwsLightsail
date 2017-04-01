from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session


@app.route('/departments/<int:dept_id>/edit/', methods=['GET', 'POST'])
def editDepartment(dept_id):
    return "This page is to edit dept_id %s" % dept_id
