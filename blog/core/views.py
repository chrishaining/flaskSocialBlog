from flask import Blueprint, Flask, redirect, render_template, url_for
from blog import db
from blog.models import User
# from blog.users.forms import LoginForm, RegistrationForm

core_blueprint = Blueprint('core', __name__)

@core_blueprint.route('/')
def index():
    return render_template('index.html')
