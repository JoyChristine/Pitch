import os 

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pitch:mypass@localhost/work'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'Secretkey'
    SESSION_COOKIE_SECURE = False
    # email configs
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("devpythonflask@gmail.com")
    MAIL_PASSWORD = os.environ.get("@whysoserious?")
   
    WTF_CSRF_ENABLED = False


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