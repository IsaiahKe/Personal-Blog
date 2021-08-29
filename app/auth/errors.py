from app.main.error import notfound
from flask import render_template
from . import auth

@auth.app_errorhandler(404)
def notfound(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('auth/notfound.html'),404