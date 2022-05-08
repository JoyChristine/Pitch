import os 

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pitch:mypass@localhost/work'
    SECRET_KEY = 'Secretkey'
    


class ProdConfig(Config):
    pass
        

class DevConfig(Config):
    
    DEBUG = True


# class TestCase(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jk:0000@localhost/pitch'
#     DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}