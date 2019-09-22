from app import db,login_manager
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin
today_f = datetime.now()
today = today_f.strftime("%d %m %Y")
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), nullable = False, unique = True)
    email = db.Column(db.String(255), nullable = False, unique = True)
    password = db.Column(db.String(255), nullable = False)
    profile_photo = db.Column(db.String(255), nullable = True )
    blogs = db.relationship('Blog',backref='user',lazy = 'dynamic')
    comments = db.relationship('Comment', backref = 'user' , lazy= 'dynamic')
    upvote = db.relationship('Upvote', backref = 'user', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='user', lazy = 'dynamic')
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self,password):
        password_hash = generate_password_hash(password)
        self.password = password_hash

    def verify_password(self,password):
        return check_password_hash(self.password,password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Blog(db.Model):
    __tablename__ = "blogs"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    blog_img = db.Column(db.String(255), nullable = False)
    blog_content = db.Column(db.Text, nullable = False)
    pub_date = db.Column(db.String(255), nullable = False,default = today)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable = False)
    comment = db.relationship('Comment', backref='blog' , lazy = 'dynamic')
    upvote = db.relationship('Upvote', backref= 'blog', lazy='dynamic')
    downvote = db.relationship('Downvote', backref='blog', lazy = 'dynamic')
    # hash_tags = db.relationship('Hashtag', backref='blog', lazy = 'dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False )
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'), nullable = False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# class Hashtag(db.Model):
#     __tablename__ = 'hashtags'
#     id= db.Column(db.Integer,primary_key = True)
#     tag = db.Column(db.String(200),nullable = False)
#     post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable = False)
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()

class Upvote(db.Model):
    __tablename__ = 'upvotes'
    id = db.Column(db.Integer, primary_key = True)
    vote = db.Column(db.String(255), nullable = False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key = True)
    vote = db.Column(db.String(255), nullable = False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
