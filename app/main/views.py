from flask import render_template
from . import main
from flask_login import login_required
from flask_login import login_required, current_user

from .. import db

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Blog'

    return render_template('index.html',title = title)
