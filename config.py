class Config(object):
    """ Parent configuration """
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/gem_wallets?unix_socket=/opt/lampp/var/mysql/mysql.sock'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'W9Vg183GAn7wvMbcCd7ALx65Wwfj1Qol5BW5xKq40sQi8OWwttHdqMcQupsNMckP'
    DEBUG = True
    TESTING = True