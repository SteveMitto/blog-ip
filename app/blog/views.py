from . import blog
from flask import render_template,jsonify,request,url_for,g
from flask_login import login_required,current_user
from app.models import Blog,Comment
from app import photos
user = current_user

@blog.route('/blog/home')
@login_required
def index():
    blogs = Blog.query.all()
    return render_template('blog/index.html', blogs = blogs)

@blog.route('/blog/add_blog', methods=['POST','GET'])
@login_required
def add_blog():
    if request.method == 'POST':
        form = request.form
        title = form.get('title')
        blog_content = form.get('blog')

        if title == None or blog_content == None :
            print("error")
            return jsonify({'error':'passwords dont match'})
        if title == ' ' or blog_content == ' ' :
            print("error")
            return jsonify({'error':'passwords dont match'})
        print("passed")
        blog_img= None
        try:
            print(form.get('blog_img'))
            filename = photos.save(request.files['blog_img'])
            path = 'photos/blog/{}'.format(filename)
            blog_img = pathA
            print(blog_img)
        except Exception as e:
            blog_img= 'photos/blog/default.jpeg'
        blog = Blog(title = title, blog_img = blog_img, blog_content = blog_content,user_id =user.id )
        blog.save()
        return jsonify({'success':'Your blog was posted'})
    return render_template('blog/add_blog.html')

@blog.route('/blog/<blog_id>/details')
def blog_details(blog_id):
    blog =Blog.query.filter_by(id = blog_id).first()
    return render_template('blog/blog_details.html',blog = blog)

@blog.route('/blog/<blog_id>/save_comment', methods=['POST'])
def save_comment(blog_id):
    comment = request.form.get('comment')
    print(comment)
    if comment == '' or None:
        return jsonify({'error':'Add a comment please'})
    new_comment = Comment(comment = comment, user_id = user.id , blog_id = blog_id)
    new_comment.save()
    return jsonify({'success':'Your comment was added'})
