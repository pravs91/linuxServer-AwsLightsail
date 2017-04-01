from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session


@app.route('/departments/new/', methods=['GET', 'POST'])
def newDepartment():
    return "This page is to create a new department."
