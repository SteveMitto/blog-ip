from . import blog
from flask import render_template,jsonify,request,url_for,redirect
from flask_login import login_required,current_user
from app.models import Blog,Comment,Upvote,Quote,StrangeComment,User
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
        filename = photos.save(request.files['blog-img'])
        path = 'photos/blog/{}'.format(filename)
        blog_img = path
        print(blog_img)
        if blog_img == None:
            blog_img= 'photos/blog/default.jpeg'
        blog = Blog(title = title, blog_img = blog_img, blog_content = blog_content,user_id =user.id )
        blog.save()
        blog = Blog.query.filter_by(title = title).first()
        return redirect(url_for('blog.blog_details',blog_id =blog.id))
        # return jsonify({'success':'Your blog was posted','id':blog.id})
    return render_template('blog/add_blog.html')

@blog.route('/blog/<blog_id>/details')
def blog_details(blog_id):
    upvotes = Upvote.query.filter_by(blog_id =blog_id).all()
    blog =Blog.query.filter_by(id = blog_id).first()
    return render_template('blog/blog_details.html',blog = blog,upvotes=upvotes)

@blog.route('/blog/<blog_id>/save_comment', methods=['POST'])
def save_comment(blog_id):
    comment = request.form.get('comment')
    print(comment)
    if comment == '' or None:
        return jsonify({'error':'Add a comment please'})
    new_comment = Comment(comment = comment, user_id = user.id , blog_id = blog_id)
    new_comment.save()
    comment_id = Comment.query.filter_by(comment = comment, user_id = user.id , blog_id = blog_id).first()
    return jsonify({
        'success':'Your comment was added',
        'comment':comment,
        'username':user.username,
        'id':comment_id.id,
        'blog_id':blog_id
        })

@blog.route('/blog/<blog_id>/delete/<comment_id>/comment')
def delete_comment(comment_id,blog_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    if blog.user.id  == user.id:
        comment = Comment.query.filter_by(id = comment_id).first()
        if comment == None:
            return redirect(url_for('blog.blog_details',blog_id = blog_id))
            # return jsonify({'error':'sorry that comment was already deleted'})
        else:
            comment.delete()
            # return jsonify({'success':'Comment deleted'})
            return redirect(url_for('blog.blog_details',blog_id = blog_id))

    else:
        abort(404)

@blog.route('/blog/<blog_id>/upvote')
def upvote(blog_id):
    upvote = Upvote.query.filter_by(user_id = user.id, blog_id=blog_id).first()
    if upvote != None:
        upvote.delete()
        return jsonify({'remove':True})
    else:
        upvote = Upvote(vote = True,user_id =user.id,blog_id =  blog_id)
        try:
            upvote.save()
            return jsonify({'success':True})
        except Exception:
            return jsonify({'success':False})

@blog.route('/blog/edit/<blog_id>', methods=['POST','GET'])
def edit_blog(blog_id):
    blog_m = Blog.query.filter_by(id = blog_id).first()

    if blog_m == None:
        return redirect(url_for('blog.blog_details', blog_id = blog_id))
    else:
            form = request.form
            title = form.get('title')
            blog = form.get('blog')
            blog_m.title= title
            blog_m.blog_content = blog
            blog_m.save()
            return jsonify({'success':True,'title':title,'blog':blog})
    return redirect(url_for('blog.blog_details', blog_id = blog_id))

@blog.route('/blog/<blog_id>/delete')
def delete_blog(blog_id):
    blog = Blog.query.filter_by(id = blog_id ).first()
    if user == blog.user:
        blog.delete()
        return redirect(url_for('blog.index'))
    else:
        abort(404)

@blog.route('/blog/stranger/comment/<blog_id>', methods=['POST','GET'])
def strange_c(blog_id):
    if request.method == "POST":
        form = request.form
        name =form.get('name')
        comment = form.get('comment')
        new_comm = StrangeComment(name = name, comment= comment,blog_id = blog_id)
        new_comm.save()
    return redirect(url_for('blog.blog_details', blog_id = blog_id))

@blog.route('/blog/<blog_id>/delete/stranger/<comment_id>/comment')
def delete_strange_comment(comment_id,blog_id):
    comment= StrangeComment.query.filter_by(id =comment_id).first()
    comment.delete()
    return redirect(url_for('blog.blog_details', blog_id = blog_id))

@blog.route('/profile', methods=['POST','GET'])
def profile():
    if current_user.is_authenticated:
        blogs = Blog.query.filter_by(user_id = user.id).all()
        return render_template('profile.html',user=user)
    else:
        abort(404)

@blog.route('/profile/save/profile-photo/<int:uid>', methods=['POST','GET'])
@login_required
def save_photo(uid):
    if 'profile' in request.files:
        filename = photos.save(request.files['profile'])
        path =  f'photos/blog/{filename}'
        user = User.query.filter_by(id = uid).first()
        if user != None:
            user.profile_photo = path
            user.save()
            return redirect(url_for('blog.profile'))
    return redirect(url_for('blog.profile'))
