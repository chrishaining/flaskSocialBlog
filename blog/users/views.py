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

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully.')
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)
