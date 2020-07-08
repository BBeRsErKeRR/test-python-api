import logging
import os
from flask import Flask

__version__ = "^__VERSION__^"
__all__=['__version__']

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

def init_app(app):
    pass

def configure_app(app, config_class, config_env_var=None):
    pass

def register_blueprints(app):
    @app.route('/')
    def home():
        logger.info("test log statement")
        logger.info("test log statement with extra props", extra={'props': {"extra_property": 'extra_value'}})
        return "hello world"

    
    @app.route('/exception')
    def exception():
        try:
            raise RuntimeError
        except BaseException as e:
            logger.error("Error occurred", exc_info=e)
            logger.exception("Error occurred", exc_info=e)
        return "Error occurred, check log for detail"


def create_app(config_class, config_env_var=None):
    app = Flask(__name__,
        instance_path=None,
        create_instance_folder=False,
        instance_relative_config=False
    )
    init_app(app)
    configure_app(app, config_class, config_env_var)
    register_blueprints(app)

    return app