import logging
# import os
import sys
from flask import Flask
from app.api.routes import api

__version__ = "^__VERSION__^"
__all__ = ['__version__']

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


def init_app(app):
    logger.info("init_app")


def configure_app(app, config_class, config_env_var=None):
    logger.info("configure_app")


def register_blueprints(app):
    app.register_blueprint(api, url_prefix='/api')


def create_app(config_class, config_env_var=None):
    app = Flask(__name__, instance_path=None, instance_relative_config=False)
    init_app(app)
    configure_app(app, config_class, config_env_var)
    register_blueprints(app)
    return app
