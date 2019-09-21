from . import auth
from flask import render_template,jsonify,redirect,url_for,request
from werkzeug.security import check_password_hash
from app.models import User
from flask_login import login_user,logout_user
@auth.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == "POST":
        form = request.form
        username =form.get('username')
        email = form.get('email')
        password = form.get('password')
        confirm_password = form.get('confirm_password')
        print(password)
        if username == None or email == None or password == None  or confirm_password == None :
            return jsonify({'error':'Fill all fields'})
        if password != confirm_password:
            return jsonify({'password_error':'passwords dont match'})
        user = User.query.filter_by(username = username).first()
        if user == None:
            user = User.query.filter_by(email = email).first()
            if user == None:
                new_user = User(username = username, email = email)
                new_user.set_password(password)
                new_user.save()
                return jsonify({'success':True})
            else:
                return jsonify({'email_error':'Email already Taken'})
        else:
            return jsonify({'username_error':'Username aready taken'})
    return render_template('auth/signup.html')

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        form = request.form
        username = form.get('username')
        password = form.get('password')
        if username == None or password == None:
            return jsonify({'error':'fill all fields'})
        user = User.query.filter_by(username = username).first()
        if user != None and user.verify_password(password):
            login_user(user)
            return jsonify({'success':True})
        else:
            return jsonify({'error':'Invalid Username or password'})
    return render_template('auth/login.html')

@auth.route('/logout')
def logout():
    logout_user()
    return render_template('auth/login.html')
