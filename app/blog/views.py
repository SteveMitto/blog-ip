from . import blog
from flask import render_template
from flask_login import login_required

@blog.route('/blog/home')
@login_required
def index():
    return render_template('blog/index.html')
