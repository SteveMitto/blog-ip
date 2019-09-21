from . import auth
from flask import render_template,jsonify,redirect,url_for,request
from app.models import User
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
