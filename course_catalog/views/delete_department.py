from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc
from sqlalchemy.exc import DBAPIError, SQLAlchemyError
from flask import session as login_session
from user_utils import login_required


@app.route('/departments/<int:dept_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteDepartment(dept_id):
    try:
        # retrieve dept to delete
        dept_to_delete = session.query(Department).filter_by(id=dept_id).one()
        departments = session.query(Department).order_by(asc(Department.name))
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404! Requested URL was not found."

    # check if dept belongs to curr user
    if dept_to_delete.user_id != login_session['user_id']:
        flash("You do not have permissions to delete %s" % dept_to_delete.name)
        return redirect(url_for('viewDepartment', dept_id=dept_to_delete.id))

    if request.method == 'POST':
        # delete courses of this dept
        dept_courses = session.query(Course).filter_by(department_id=dept_id)
        for course in dept_courses:
            session.delete(course)
        # delete dept
        session.delete(dept_to_delete)
        flash("You have successfully deleted '%s'" % dept_to_delete.name)
        session.commit()
        return redirect(url_for('showDepartments'))
    else:
        return render_template("delete_dept.html", departments=departments,
                               name=dept_to_delete.name)
