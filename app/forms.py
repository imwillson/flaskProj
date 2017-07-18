from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# this was imported
# forms.py is called by the view to and renders the loginForm
class LoginForm(Form):
	# DataRequired checks if the field is empty or not
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)