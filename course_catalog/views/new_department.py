from course_catalog import app
import course_catalog.models
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from flask import session as login_session


@app.route('/departments/new/', methods=['GET', 'POST'])
def newDepartment():
    # if 'username' not in login_session:
    #     return redirect('/')
    if request.method == 'POST':
        pass
    else:
        return render_template("new_department.html")
