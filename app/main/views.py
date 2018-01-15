from flask import render_template
from . import main
from flask_login import login_required
from flask_login import login_required, current_user
from .forms import RegistrationForm, LoginForm

from .. import db

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')
    return render_template('index.html', login_form = login_form )
