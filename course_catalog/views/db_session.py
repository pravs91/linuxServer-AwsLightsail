from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from course_catalog.models import Base

# Connect to Database and create database session
engine = create_engine('postgresql://catalog:udacity@localhost/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
