from flask import render_template
from app import app 

# view function wrapped to this route 
@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Willson'}
	posts = [
		{ 
		'author': {'nickname': 'John'}, 
		'body': 'Beautiful day in Portland!' 
		},
		{ 
		'author': {'nickname': 'Susan'}, 
		'body': 'The Avengers movie was so cool!' 
		}

	]
	return render_template('index.html', 
							title='Home',
							user=user, 
							posts=posts) 
	# these are positional arguments, passed in from 
	# the funciont


