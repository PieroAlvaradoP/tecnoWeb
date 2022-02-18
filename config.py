from app.utils.logging import file_logger, client_logger
from decouple import config as env_conf
import logging

class LocalPSQLConfig:
    DB_USER = env_conf('DATABASE_USER')
    DB_PASSWORD = env_conf('DATABASE_PASS')
    DB_HOST = env_conf('DATABASE_HOST')
    DB_PORT = env_conf('DATABASE_PORT')
    DB_NAME = env_conf('DATABASE_NAME')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.\
        format(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

    SECRET_KEY = env_conf("SECRET_KEY", cast=str, default="123456")

    @classmethod
    def init_app(cls, app):
        app.logger.setLevel(logging.DEBUG)
        app.logger.addHandler(file_logger)
        app.logger.addHandler(client_logger)

class Develop:
    DB_USER = "postgres"
    DB_PASSWORD = "123456"
    DB_HOST = "localhost"
    DB_PORT = "5432"
    DB_NAME = "GestionONG"
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    SECRET_KEY = env_conf("SECRET_KEY", cast=str, default="12345")

    @staticmethod
    def init_app(app):
        app.logger.setLevel(logging.DEBUG)
        app.logger.addHandler(client_logger)
        app.logger.addHandler(file_logger)

config_dict = {
    'localpsql': LocalPSQLConfig,
    'develop': Develop,
}
