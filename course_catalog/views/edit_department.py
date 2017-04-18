from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc
from sqlalchemy.exc import DBAPIError, SQLAlchemyError
from flask import session as login_session


@app.route('/departments/<int:dept_id>/edit/', methods=['GET', 'POST'])
def editDepartment(dept_id):
    if 'username' not in login_session:
        flash("Please login to continue.")
        return redirect('/login')
    try:
        # retrieve dept to edit
        dept_to_edit = session.query(Department).filter_by(id=dept_id).one()
        departments = session.query(Department).order_by(asc(Department.name))
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404! Requested URL was not found."

    # check if dept belongs to curr user
    if dept_to_edit.user_id != login_session['user_id']:
        flash("You do not have permissions to edit %s") % dept_to_edit.name
        return redirect(url_for('viewDepartment', dept_id=dept_to_edit.id))

    if request.method == 'POST':
        dept_to_edit.name = request.form['name']
        dept_to_edit.address = request.form['address']
        dept_to_edit.img_url = request.form['img_url']
        dept_to_edit.description = request.form['description']
        flash("You have successfully edited %s" % dept_to_edit.name)
        return redirect(url_for('viewDepartment', dept_id=dept_id))
    else:
        return render_template("new_department.html", departments=departments,
                               name=dept_to_edit.name,
                               address=dept_to_edit.address,
                               img_url=dept_to_edit.img_url,
                               description=dept_to_edit.description,
                               edit=True)
