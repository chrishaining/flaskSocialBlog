from blog import app, db
from blog.models import User
from blog.users.forms import LoginForm, RegistrationForm
from flask import Blueprint, Flask, render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('core.index'))
    return render_template('register.html', form=form)
