import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
	""" Opens a database connection """
	conn = sqlite3.connect('mydb.sqlite')
	conn.row_factory = sqlite3.Row
	return conn

app = Flask(__name__)

@app.route('/')
def index():
	conn = get_db_connection() # opens the db connection
	movies = conn.execute('SELECT * FROM movies').fetchall() # executes sql query to get all posts from the table
	conn.close()
	return render_template('index.html', movies=movies) # passes the posts as an argument to access blog posts in index.html template