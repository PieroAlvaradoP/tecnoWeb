# noinspection PyUnresolvedReferences
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config_dict

db = SQLAlchemy()


def create_app(config_key='local'):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_key])
    config_dict[config_key].init_app(app)
    db.init_app(app)

    from app.main._init_ import main as main_blueprint
    #    from app.main._init_ import api_bp as api_blueprint

    app.register_blueprint(main_blueprint)
    #   app.register_blueprint(api_blueprint)

    with app.app_context():
        db.create_all()
    return app
