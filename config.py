import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY')
        MAIL_SERVER = os.environ.get('MAIL_SERVER')
        MAIL_PORT = os.environ.get('MAIL_PORT')
        MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
        MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


        @staticmethod
        def init_app(app):
                pass

    