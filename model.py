from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Song(Base):
	__tablename__ = 'song'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	artist = Column(String)
	album = Column(String)
	year = Column(Integer)
	username = Column(String)



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True)
    password = Column(String)
    def __repr__(self):
        return("username: {}, password: {}".format(self.username,self.password))