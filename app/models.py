from app import db
# from the app module (which is a folder), import the db initated in __init__.py

class User(db.Model):
	# id is the primary key, it is also integer value
	# primary key is automatically set, primary key
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	
	# relationship to foreign key (one user, many posts one to many relationship)
	# what is backref author 
	posts = db.relationship('Post', backref='author', lazy='dynamic')


	# print for debugging
	def __repr__(self):
		return '<User %r>' % (self.nickname)

# user_id is the foreign key
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self): 
		return '<Post %r>' % (self.body)
