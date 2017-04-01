from sqlalchemy import create_engine
from models import *

engine = create_engine('sqlite:///course_catalogue_datastore.db')
Base.metadata.create_all(engine)
