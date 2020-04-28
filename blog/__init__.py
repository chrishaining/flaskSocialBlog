from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True


###############
### CONFIGS ###
###############
app.config['SECRET_KEY'] = 'mykey'

# set up Debug sidebar
toolbar = DebugToolbarExtension(app)

################################
##### SQL DATABASE SECTION #####
import os
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


# pass the app to the loginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login' # this will be one of the views (routes)

# register blueprints
from blog.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/users')

from blog.core.views import core_blueprint
app.register_blueprint(core_blueprint, url_prefix='/core')
