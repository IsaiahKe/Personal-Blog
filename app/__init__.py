from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

#initialization decalarations
bootstrap=Bootstrap()
login_manager=LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'
db=SQLAlchemy()
mail=Mail()




def create_app(config_name):
    app= Flask(__name__)
    app.config.from_object(config_options[config_name])
    
    
    bootstrap.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    #register main class blueprint application
    from .main import main as main_blueprint
    app .register_blueprint(main_blueprint)
    #register auth blue print to main
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,prefix='/auth')
    
    
    
    return app