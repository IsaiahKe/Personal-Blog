from flask import render_template, redirect, url_for,flash,request
from flask_login import login_user, login_required,logout_user,current_user
from . import auth

from .forms import LoginForm, RegistrationForm,PostForm,CommentForm,SubscriberForm
from ..models import User,Post,Comment,Subscribe
from .. import db


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    title = 'Login'
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.password_verification(
                form.password.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid Credentials!')

    return render_template('auth/login.html', form=form, title=title)


@auth.route('/register', methods=['POST', 'GET'])
def register():
    title = 'Registration'
    register = RegistrationForm()
    if register.validate_on_submit():
        user = User(username=register.name.data,
                    email=register.email.data,
                    phone=register.phone.data,
                    password=register.password.data)
       

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', register=register, title=title)


@auth.route('/profile')
@login_required
def profile():

    return render_template('auth/update.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/addpost',methods=['POST','GET'])
@login_required
def addpost():
    currentUser=current_user.username
    addpost= PostForm()
    if addpost.validate_on_submit():
        post=Post(topic=addpost.topic.data,content=addpost.content.data,owner=currentUser)
     
        
        post.save()
       
        return redirect(url_for('main.index'))
    return render_template('auth/post.html',addpost=addpost,user=currentUser)

@auth.route('/<postid>/comment',methods=['POST','GET'])
@login_required
def comment(postid):
    
    postitem=Post.query.filter_by(id=postid).first()
    postowner=postitem.owner
    user=current_user.username
    items=Comment.query.filter_by(parentid=postid).all()
    form=CommentForm()
    if form.validate_on_submit():
        post=Comment.query.filter_by(id=postid)
        if post:
            usercomment=form.comment.data
           
           
            feedback= Comment(content=usercomment,owner=user)
            feedback.save()
            return redirect(url_for('main.index'))
            
    return render_template('auth/comment.html',form=form,item=items,postowner=postowner,user=user)

    
    
@auth.route('/Subscribe',methods=['GET','POST'])
def subsblog():
    
    form = SubscriberForm()
    if form.validate_on_submit():
        subs = Subscribe(email = form.email.data, username = form.username.data)    
        db.session.add(subs)
        db.session.commit()

        return redirect(url_for('main.index'))
    return render_template('auth/subscribe.html',subscribe_form=form)

@auth.route('/<commentid>/delete')
def delete(commentid):
    comment=Comment.query.filter_by(id=commentid).delete()
    
    
    db.session.commit()
    return redirect(url_for('auth.comment'))
