from model import *
from  sqlalchemy.sql.expression import func, select
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()

RANDOM_SONG_NUMBER = 2



def add_song(name,artist,album,year, username):
    print("Added song!")
    song_o = Song(name = name, artist = artist, album = album, year = year, username = username)
    session.add(song_o)
    session.commit()

# def delete_song(id):
# 	session.query(Company).filter_by(id=id).first().delete()


def update_song(id,name,artist,album,year):
    song_o = session.query(
    song).filter_by(
        id=id).first()
    song_o.name = name
    song_o.artist = artist
    song_o.album = album
    song_o.year = year
    session.commit()





def add_user(user_username, user_password):
	user1 = User(username = user_username, password = user_password)
	session.add(user1)
	session.commit()

def check_user(username, password):
	user = session.query(User).filter_by(
	username=username).first()
	if user !=None:
		if(user.password==password):
			return(True)

def getRandomSongs():
	song_list = session.query(Song).order_by(func.random()).limit(RANDOM_SONG_NUMBER)
	return song_list

def getMySongs(username):
	song_list = session.query(Song).filter_by(username = username).all()
	return song_list

def query_by_username(username):
	user = session.query(User).filter_by(
		username = username).first()
	return user