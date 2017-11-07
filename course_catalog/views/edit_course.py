from course_catalog import app
from course_catalog.models import *
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from db_session import session
from sqlalchemy import asc, and_
from sqlalchemy.exc import DBAPIError, SQLAlchemyError
from flask import session as login_session
from user_utils import login_required


@app.route('/departments/<int:dept_id>/courses/<course_id>/edit/', methods=['GET', 'POST'])  # NOQA
@login_required
def editCourse(dept_id, course_id):
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
        # check only if new id is different from old id
        id_exists = (id != course_id) and session.query(
            Course).filter_by(id=id).count() > 0
        if id_exists:
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

        curr_course.name = name
        curr_course.id = id
        curr_course.professor = professor
        curr_course.img_url = img_url
        curr_course.credits = credits
        curr_course.max_capacity = max_capacity
        curr_course.description = description
        session.commit()
        flash("You have successfully edited %s" % curr_course.name)
        return redirect(url_for('viewCourse', dept_id=dept_id, course_id=curr_course.id))
    else:
        return render_template("new_course.html", departments=departments,
                               curr_dept=curr_dept,
                               name=curr_course.name,
                               id=curr_course.id,
                               professor=curr_course.professor,
                               img_url=curr_course.img_url,
                               credits=curr_course.credits,
                               max_capacity=curr_course.max_capacity,
                               description=curr_course.description,
                               edit=True)


def report_error(fields, error):
    return render_template("new_course.html", departments=fields[0],
                           curr_dept=fields[1], name=fields[2],
                           id=fields[3], professor=fields[4],
                           img_url=fields[5], credits=fields[6],
                           max_capacity=fields[7], description=fields[8],
                           error=error)
