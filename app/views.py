from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from .forms import LoginForm # period is file structure
from .models import User

# view function wrapped to this route 
# login required is a property, if this isn't true, the uesr won't have access to the posts
@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
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
#login handler for login
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler 
def login():
	# g stores the login data
	# if there is already a logged in user - go to index
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))

	# LoginForm Class / how it renders
	form = LoginForm()

	#validate_on_submit does all the validation
	# tries to logina fter all is validated
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])

		# flash shows a message on the next page
		# %s is for string 
		# flash('Login requested for OpenID="%s", remember_me=%s' %
		# 	(form.openid.data, str(form.remember_me.data)))
		# return redirect('/index')

	return render_template('login.html', 
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS']) 
							# we pass form (the data) \
							# into this template 

# the resp apssed into this function is the information held after login
@oid.after_login
def after_login(resp):

    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()

    # sets up a new user if the email is recognized
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)

    # after logging in, goes to next page (allows for all pages to be accessed)
    return redirect(request.args.get('next') or url_for('index'))

# this a decorator , so it runs load_user through the lm.user_loader
@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

#forces the app to run this property decorator 
# checks for a g.user ... current user is set by flask login
@app.before_request
def before_request():
    g.user = current_user

