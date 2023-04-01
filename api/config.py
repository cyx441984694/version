class Config(object):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678@localhost:3306/version_control_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
