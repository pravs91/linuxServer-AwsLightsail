from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session


@app.route('/')
@app.route('/departments/')
def showDepartments():
    return render_template("base.html")
    # return "Hello, Praveen!"
