from flask import Flask
app = Flask(__name__)
# app variable and app package not the same

# from the app instantiated, get the views.py file
from app import views
# views handle the requests from web