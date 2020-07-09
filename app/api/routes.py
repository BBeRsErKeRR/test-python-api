from . import api
import logging

logger = logging.getLogger(__name__)

@api.route('/')
def home():
    logger.info("test log statement")
    logger.info("test log statement with extra props", 
        extra={'props': {"extra_property": 'extra_value'}}
        )
    return "hello world"

@api.route('/exception')
def exception():
    try:
        raise RuntimeError
    except BaseException as e:
        logger.error("Error occurred", exc_info=e)
        logger.exception("Error occurred", exc_info=e)
    return "Error occurred, check log for detail" , 400