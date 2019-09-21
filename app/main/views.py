from . import main
from flask import render_template
from flask_login import login_required
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/contact-us')
def contact():
    return render_template('contact-us.html')

@main.route('/about-us')
def about():
    return render_template('about-us.html')
