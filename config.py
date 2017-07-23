import os

WTF_CSRF_ENABLED = True
SECRET_KEY ='you-will-never-guess'

# used by the init file to enable CSRF configuration



OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


basedir = os.path.abspath(os.path.dirname(__file__))

# file pathing for the directory of database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# migrating is used for tracking changes / updates for 
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, '_db_repository')

