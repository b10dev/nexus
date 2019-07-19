from flask import Blueprint, render_template, request, url_for, flash, redirect
from nexus.login.forms import LoginForm

login = Blueprint('login', __name__)


@login.route('/')
def loginpage():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login/login.html', title='Login', form=form)
