from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc, and_
from sqlalchemy.exc import DBAPIError, SQLAlchemyError
from flask import session as login_session
from user_utils import login_required


@app.route('/departments/<int:dept_id>/courses/<course_id>/delete/', methods=['GET', 'POST'])  # NOQA
@login_required
def deleteCourse(dept_id, course_id):
    # retrieve course for given dept from DB
    try:
        departments = session.query(Department).order_by(asc(Department.name))
        curr_dept = session.query(Department).filter_by(id=dept_id).one()
        dept_courses = session.query(Course).filter_by(department_id=dept_id)
        curr_course = session.query(Course).filter(
            and_(Course.id == course_id, Course.department_id == dept_id)).one()
    # handle database exceptions
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404, requested URL was not found! Exception occured in Database."

    # check if course belongs to current user
    if curr_course.user_id != login_session['user_id']:
        flash("You do not have permissions to edit this course.")
        return redirect(url_for('viewCourse', dept_id=dept_id, course_id=course_id))

    if request.method == 'POST':
        session.delete(curr_course)
        flash("You have successfully deleted %s - %s" %
              (curr_course.id, curr_course.name))
        session.commit()
        return redirect(url_for('viewDepartment', dept_id=dept_id))
    else:
        return render_template("delete_course.html", departments=departments,
                               id=curr_course.id, name=curr_course.name)
