from . import auth
from flask import render_template
@auth.route('/signup')
def signup():
    return "hello world"
