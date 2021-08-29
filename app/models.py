
from . import db
from werkzeug.security import check_password_hash,generate_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
class Quote:
    def __init__(self,author,id,quote,permalink):
        self.author=author
        self.id=id
        self.quote=quote
        self.permalink=permalink
        


class User(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50),index=True)
    email=db.Column(db.String(60),index=True)
    phone=db.Column(db.Integer,index=True)
    encrypedtedpassword=db.Column(db.String(255),index=True)
    
    @property
    def password(self):
        raise AttributeError ("Encripting")
    @password.setter
    def password(self,password):
        self.encrypedtedpassword = generate_password_hash(password)
        
    def password_verification(self,password):
        return check_password_hash(self.encrypedtedpassword,password)
    
    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(int(user_id))
    
    def __repr__(self):
        return f'User{self.username}'
    
class Subscribe(db.Model):
    __tablename__='subscribers'
    id=db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(50),nullable=False)
    postid=db.Column(db.Integer,nullable=False)
    
    def __repr__(self):
        return f'Subscribe{self.email}'
    
class Post(db.Model):
    __tablename__="posts"
    id=db.Column(db.Integer,primary_key=True)
    topic= db.Column(db.String(255),nullable=False)
    content=db.Column(db.String())
    posted=db.Column(db.DateTime,default=datetime.now)
    owner=db.Column(db.String(50))
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f'Post{self.content}'
class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(255), index=True)
    parentid=db.Column(db.Integer,db.ForeignKey('posts.id'))
    owner=db.Column(db.String(50))
    def save(self):
        db.session.add(self)
        db.session.commit()
    def __repr__(self):
        return f'Comment{self.content}'
    