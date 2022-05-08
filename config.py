import os 

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nduta:0000@localhost/watchlist'


    SECRET_KEY = 'Secretkey'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'devpythonflask@gmail.com'
    MAIL_PASSWORD = '@whysoserious?'
    


class ProdConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #     SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)
        

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}