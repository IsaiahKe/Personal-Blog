from flask import render_template
from app.requests import get_quote
from . import main
from ..models import Comment,Post
from flask_login import current_user
from sqlalchemy import desc,select
from flask_login import current_user,login_required

@main.route('/')
def index():
    
    title="home"
    quote=get_quote()
    posts= Post.query.order_by(Post.posted.desc())
    
    return render_template('index.html',title=title,quote=quote,posts=posts)
