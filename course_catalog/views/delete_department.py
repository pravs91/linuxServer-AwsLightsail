from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session


@app.route('/departments/<int:dept_id>/delete/', methods=['GET', 'POST'])
def deleteDepartment(dept_id):
    return "This page is to delete dept_id %s" % dept_id
