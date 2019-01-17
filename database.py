from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()

def function(parameter):
    pass

class song(Base):
	__tablename__ = 'songs'
    	id = Column(Integer, primary_key = True) 
    	name = Column(String)
		artist = Column(String)
		album = Column(String)
		year = Column(Integer)	 

def add_student(name, year, finished_lab):