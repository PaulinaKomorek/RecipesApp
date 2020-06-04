from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

SQLALCHEMY_DATABASE_URI = config.get('DATABASE', 'URI')
SQLALCHEMY_TRACK_MODIFICATIONS = config.get('SQLALCHEMY', 'modifications')