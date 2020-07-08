import os
import jsonlogging
from app import __verxion__

LOG_FORMATER = os.environ.get('LOG_FORMATER', 'default')
LOGLEVEL = os.environ.get('LOGLEVEL', 'info')