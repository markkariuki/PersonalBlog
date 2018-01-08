from flask import render_template
from . import main
from flask_login import login_required

#views
@main.route('/')
def index():

    return render_template('index.html')

@main.route('/c/')
@login_required
def new_review(id):
    pass
