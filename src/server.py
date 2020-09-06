# coding: utf-8
from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3
import hashlib
import re

md5 = lambda s: hashlib.md5(s.encode('utf8')).hexdigest()

users = ["noob", "alice", "bob", "carl", "dania"]
"""
Passwords:
noob:SoccerMom2007
alice:704-186-9744
bob:5809be03c7cc31cdb12237d0bd718898
carl:DionysusDelaware
dania:طاووسة 
"""



flag_parts = {
	"noob": "uiuctf{Dump",
	"alice": "_4nd_un",
	"bob": "h45h_63",
	"carl": "7_d4t_",
	"dania": "c45h}"
}

def search_database(query):
	if not query: return 
	try:
		sql_command = "select username, bio from users where username like \"%" + query + "%\""
		print(sql_command)
		con = sqlite3.connect("password.db", uri=True)
		cur = con.cursor()
		response = cur.execute(sql_command).fetchall()
		return response
	except Exception as e:
		print(e)
		return "error"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	password_hint = None
	if request.method == 'POST':
		try:
			username = request.form['username']
			password = request.form['password']
			con = sqlite3.connect("password.db", uri=True)
			cur = con.cursor()
			response = cur.execute("SELECT username FROM users WHERE username == \""+str(username)+"\" AND password_hash == \""+str(md5(password))+"\";").fetchall()
			if len(response) == 0:
				error = 'Invalid Credentials. Please try again.'
				if username in users:
					response = cur.execute("SELECT hint FROM users WHERE username == \"" + str(username) + "\"").fetchall()
					password_hint = response[0][0]
			else:
				return "You have successfully logged in! Here's part " + str(users.index(username)) + " of the flag: " + flag_parts[username] if username in flag_parts else ""
		except Exception as e:
			print(e)
			error = "Invalid input!"
	return render_template('login.html', error=error, password_hint=password_hint)

@app.route("/search", methods = ["GET", "POST"])
def search():
	response = None
	r = None
	error = False
	if request.method == "POST":
		r = request.form['request']
		response = search_database(r)
		if response == "error":
			response = None
			error = True
	return render_template("search.html", response=response, error=error)

if __name__ == '__main__':
	app.run(host="0.0.0.0")
