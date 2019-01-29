from flask import Flask, render_template, url_for, redirect, request
from flask import session as login_session
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your_secret_string"

@app.route('/')
def home():
	if (login_session.get('username')!=None):
		user1=query_by_username(login_session['username'])
		song_list = getMySongs(user1.username)
		return render_template('user.html', user1 = user1, song_list = song_list)
	else:
		return render_template('index.html')

@app.route("/Logout")
def Logout():
	login_session['username'] = None
	# del login_session['username']
	return redirect(url_for('home'))
	# # # return render_template('index.html')
		# if (login_session.get('username')!=None):
		# 	del login_session['id']
		# 	del login_session['username']
		# 	return redirect(url_for('home'))
		# else:
		# 	return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])	
def user_login():
	if request.method == 'POST':
		if (check_user(request.form['username'],request.form["password"])):
			user=query_by_username(request.form['username'])
			login_session['id']=user.id
			login_session['username']=user.username
			return redirect(url_for('home'))
		else:
			return render_template("sign in.html")
	else:
		return render_template("sign in.html")


@app.route('/adduser', methods=['GET', 'POST'])
def add_user_route():
	if request.method == 'GET':
		return render_template('sign up.html')
	else:
		if (request.form["password"]==request.form["repassword"]):
			add_user(request.form['username'],request.form["password"] )
			return redirect(url_for('home'))
		else:
			return render_template('sign up.html')

@app.route('/random_suggestions', methods = ['GET','POST'])
def random_suggestions():
	song_list = getRandomSongs()
	return render_template('random_suggestions.html', song_list = song_list)

# @app.route('/user')
# def user_page():
# 	if :
		
# 	return render_template('user.html')


@app.route('/addsong', methods=['GET', 'POST'])
def addSong():
	if request.method == 'GET':
		return render_template('add-song.html')
	else:
		name = request.form["Name"]
		artist = request.form["Artist"]
		year = request.form["Year"]
		album = request.form["Album"]
		add_song(name, artist, album, year, login_session['username'])
		return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)

