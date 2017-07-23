from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
### app variable and app package not the same
app.config.from_object('config')
db = SQLAlchemy(app)

# refers to config file
app.config.from_object('config')

# from the app instantiated, get the views.py file'
from app import views, models
# views handle the requests from web\

