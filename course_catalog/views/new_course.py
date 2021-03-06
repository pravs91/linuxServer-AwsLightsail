from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc
from flask import session as login_session
from sqlalchemy.exc import DBAPIError, SQLAlchemyError
from user_utils import login_required


@app.route('/departments/<int:dept_id>/courses/new/', methods=['GET', 'POST'])
@login_required
def newCourse(dept_id):
    # error 404 if dept not found
    try:
        departments = session.query(Department).order_by(asc(Department.name))
        curr_dept = session.query(Department).filter_by(id=dept_id).one()
    except (DBAPIError, SQLAlchemyError) as e:
        return "Error 404! Requested URL was not found."

    # check if dept belongs to current user
    if curr_dept.user_id != login_session['user_id']:
        flash("You do not have permissions to add courses to this department.")
        return redirect(url_for('showDepartments'))

    if request.method == "POST":
        name = request.form['name']
        id = request.form['id']
        professor = request.form['professor']
        img_url = request.form['img_url']
        credits = request.form['credits']
        max_capacity = request.form['max_capacity']
        description = request.form['description']

        fields = [departments, curr_dept, name, id, professor, img_url,
                  credits, max_capacity, description]

        # check if course code already exists
        id_exists = session.query(Course).filter_by(id=id)
        if id_exists.count() > 0:
            error = "This course code already exists!"
            return report_error(fields, error)

        # validate course code length
        if len(id) > 6:
            error = "Course code cannot be more than 6 characters!"
            return report_error(fields, error)

        # validate credits
        try:
            int_credits = int(credits)
            if int_credits > 5:
                raise ValueError
        except ValueError:
            error = "Please enter a valid number of credits"
            return report_error(fields, error)

        # validate capacity
        try:
            int_capacity = int(max_capacity)
        except ValueError:
            error = "Please enter a valid integer for capacity."
            return report_error(fields, error)

        # create new course and commit to DB
        try:
            new_course = Course(name=name,
                                id=id,
                                professor=professor,
                                img_url=img_url,
                                credits=credits,
                                max_capacity=max_capacity,
                                description=description,
                                department_id=dept_id,
                                user_id=login_session['user_id'])
            session.add(new_course)
            session.commit()
        # handle database exceptions
        except (DBAPIError, SQLAlchemyError) as e:
            flash("An exception occurred in the database. Please try again!")
            return redirect(url_for('showDepartments'))
        else:
            flash("Successfully created new course %s" %
                  new_course.name)
            return redirect(url_for('viewCourse', dept_id=dept_id, course_id=id))

    else:
        return render_template("new_course.html", departments=departments,
                               curr_dept=curr_dept)


def report_error(fields, error):
    return render_template("new_course.html", departments=fields[0],
                           curr_dept=fields[1], name=fields[2],
                           id=fields[3], professor=fields[4],
                           img_url=fields[5], credits=fields[6],
                           max_capacity=fields[7], description=fields[8],
                           error=error)
