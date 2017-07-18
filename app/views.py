from flask import render_template, flash, redirect
from app import app 
from .forms import LoginForm # period is file structure

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

# routes default have get requestss
@app.route('/login', methods=['GET', 'POST'])
def login():
	# LoginForm Class / how it renders
	form = LoginForm()

	#validate_on_submit does all the validation
	if form.validate_on_submit():

		# flash shows a message on the next page
		# %s is for string 
		flash('Login requested for OpenID="%s", remember_me=%s' %
			(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')

	return render_template('login.html', 
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS']) 
							# we pass form (the data) \
							# into this template 


