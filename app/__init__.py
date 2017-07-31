import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID  	 
from config import basedir

app = Flask(__name__)
### app variable and app package not the same
app.config.from_object('config')
db = SQLAlchemy(app)

# refers to config file
app.config.from_object('config')


# for login
# lm.login_view allows the interpereter to know that login is being done by lm and in the login route
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_view = 'login'

#this import has to be under the views... because these above items have to instantiated first before import the views in.. 

# from the app instantiated, get the views.py file'
from app import views, models 	
# views handle the requests from web\