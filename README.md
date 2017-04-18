# University Course Catalog
A course catalog website developed using Flask framework. SQLAlchemy Object relational mapper is used for database operations.

## Features
- Facebook and Google sign-in using OAuth2 plug-ins
- Logged in users can create, read, update and delete departments and courses
- SQLite database to support CRUD operations
- Enforce user permissions for CRUD operations

## To install and run the flask app
- Clone this repository and bring up Vagrant by typing ```vagrant up```. Refer these links to install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/)
- Navigate to the app's folder - ```cd /vagrant/catalog```
- Set up these environment variables
```
export FLASK_APP=course_catalog
export FLASK_DEBUG=true
```

- Install and run the app
```
sudo pip install -e .
flask run --host=0.0.0.0
```

## URL routing (sub-domains)
- /departments/ - Home page to view all departments
- /login/ - Login page
- /departments/new/ - create a new department
- /departments/<dept_id>/courses/ - view courses of a particular department
- /departments/<dept_id>/edit/ - edit department
- /departments/<dept_id>/delete/ - delete department
- /departments/<dept_id>/courses/new - create new course under a particular department
- /departments/<dept_id>/courses/<course_id>/ - view a particular course of a department
- /departments/<dept_id>/courses/<course_id>/edit - edit course
- /departments/<dept_id>/courses/<course_id>/delete - delete course

## JSON endpoints for the application
- /departments/JSON/ 
- /courses/JSON/
- /departments/<dept_id>/JSON/
- /departments/<dept_id>/courses/JSON/
- /departments/<dept_id>/courses/<course_id>/JSON/
