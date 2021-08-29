from flask import render_template
from . import main

@main.errorhandler(404)
def notfound():
    '''
    error function
    '''
    return render_template('notfound.html'),404
