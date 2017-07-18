#!flask/bin/python

# ^ forces run.py to run interpret from the virtualenv
# in the bin, activation forces everything to run through 
# the virtual env

from app import app
# import app function from app module
# FROM refers to the the entire folder as a module
# also know as a "package"
app.run(debug=True)
