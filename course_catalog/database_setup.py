from sqlalchemy import create_engine
from models import *

engine = create_engine('postgresql://catalog:udacity@localhost/catalog')
Base.metadata.create_all(engine)
