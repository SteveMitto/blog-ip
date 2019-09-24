from . import main
from flask import render_template
from app.models import Quote,Blog
import requests
from flask_login import login_required
@main.route('/')
def index():
    try:
        request = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
        res_json = request.json()
        author = res_json.get('author')
        quote = res_json.get('quote')
        link = res_json.get('permalink')
        quote = Quote(author,quote,link)
    except Exception:
        quote = None
    blogs = Blog.query.all()
    return render_template('index.html',quote= quote,blogs=blogs)

@main.route('/contact-us')
def contact():
    return render_template('contact-us.html')

@main.route('/about-us')
def about():
    return render_template('about-us.html')
