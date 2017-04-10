from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from flask import session as login_session
from sqlalchemy import asc
from sqlalchemy.exc import DBAPIError, SQLAlchemyError


@app.route('/departments/new/', methods=['GET', 'POST'])
def newDepartment():
    if 'username' not in login_session:
        return redirect('/')
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        img_url = request.form['img_url']
        description = request.form['description']

        try:
            newDepartment = Department(name=name, address=address, img_url=img_url,
                                       description=description,
                                       user_id=login_session['user_id'])
            session.add(newDepartment)
            session.commit()

        except (DBAPIError, SQLAlchemyError) as e:
            flash("An exception occurred in the database. Please try again!")
            return redirect(url_for('showDepartments'))
        else:
            flash("Successfully created new department %s" %
                  newDepartment.name)
            return redirect(url_for('showDepartments'))

    else:
        departments = session.query(Department).order_by(asc(Department.name))
        return render_template("new_department.html", departments=departments)
