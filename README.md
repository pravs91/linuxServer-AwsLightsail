# University Course Catalog
A course catalog website developed using Flask framework. SQLAlchemy Object relational mapper is used for database operations.
The application is deployed on an AWS Lightsail server instance.

## Server details
Public static IP - 52.26.189.38
 
URL - http://ec2-52-26-189-38.us-west-2.compute.amazonaws.com/

## Software and configuration
- Python pip
- wsgi
- Flask
- SQLAlchemy, psycopg2
- Postgres
- oathu2lib
- Configured a new user 'grader' with sudo permissions
- Configured key based SSH authentication for admin users 'grader' and 'ubuntu'
- 'grader' ssh key is at /home/grader/.ssh/authorized_keys
- Configured UFW firewall to only server ports 80 (HTTP), 123 (NTP) and 2200 (SSH)
- Disabled SSH login for root user
- Configured PostgreSQL database 'catalog' with ALTER ROLE 'catalog'
- Setup Apache to serve the wsgi application by folloowing this [link](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps)

## Features
- Facebook and Google sign-in using OAuth2 plug-ins
- Logged in users can create, read, update and delete departments and courses
- PostgreSQL database to support CRUD operations
- Enforce user permissions for CRUD operations


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
