from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from flask import session as login_session


@app.route('/departments/new/', methods=['GET', 'POST'])
def newDepartment():
    if 'username' not in login_session:
        return redirect('/')
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        imgURL = request.form['imgURL']
        description = request.form['description']

        if not (name and address and imgURL and description):
            error = "Please don't leave any fields empty."
            return render_template("new_department.html", error=error,
                                   name=name, address=address,
                                   imgURL=imgURL, description=description)
        session.rollback()
        newDepartment = Department(name=name, address=address, img_url=imgURL,
                                   description=description,
                                   user_id=login_session['user_id'])
        session.add(newDepartment)
        session.commit()
        flash("Successfully created new department %s" % newDepartment.name)
        return redirect(url_for('showDepartments'))

    else:
        return render_template("new_department.html")
