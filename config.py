import os
class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY')
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/blog'
    DEBUG=True
class ProdConfig(Config):
    pass
class TestConfig(Config):
    pass
config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'testing':TestConfig
}