from app import app 

# view function wrapped to this route 
@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"