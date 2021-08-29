from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,IntegerField,BooleanField
from wtforms import validators
from wtforms.fields.simple import TextAreaField, TextField
from wtforms.validators import Required,Email,EqualTo, ValidationError
from ..models import User,Subscribe



class LoginForm(FlaskForm):
    email =StringField(label='Enter Email Address',validators=[Required(),Email()])
    password=PasswordField(label='Enter your password',validators=[Required()])
    remember=BooleanField('Remember me')
    submit=SubmitField('Login')
    
    
    
    
class RegistrationForm(FlaskForm):
    name= StringField(label='Username',validators=[Required()])
    email =StringField(label='Enter Email Address',validators=[Required(),Email()])
    phone =IntegerField(label='User Telephone',validators=[Required()])
    password= PasswordField(label="User password",validators=[Required(),EqualTo('confirmpassword',message='The passwords does not match!')])
    confirmpassword=PasswordField(label='Confirm password',validators=[Required()])
    submit=SubmitField('Register')
    
    def check_username(self,data_field):
     if User.query.filter_by(name=data_field.data).first():
        raise ValidationError("The username is already taken!")
    def check_mail(self,data_field):  
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError("The email is already in use")
        
class PostForm(FlaskForm):
    topic=TextField('Topic',validators=[Required()])
    content=TextAreaField('post body',validators=[Required()])
    submit=SubmitField("Post")
    
class CommentForm(FlaskForm):
    comment=TextAreaField("Comment",validators=[Required()])
    submit=SubmitField('Send')
class SubscriberForm(FlaskForm):
    email = StringField('Enter your email address.',validators = [Required()])
    username = StringField('Username', validators = [Required()])
    submit = SubmitField('Subscribe')

    def validate_email(self,data_field):
        if Subscribe.query.filter_by(email = data_field.data).first():
            raise ValidationError('You are already subscribed to another post') 
class PostUpdate(FlaskForm):
    content=TextAreaField('Content',validators=[Required()])
    update=SubmitField('Update')

class TitleUpdate(FlaskForm):
    title=TextField('Title',validators=[Required()])
    update=SubmitField('Update')