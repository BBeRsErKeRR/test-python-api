import os

bind = "0.0.0.0:5000"

workers = os.environ.get('WORKERS',1)

keepalive = 2
errorlog = '-'
accesslog = '-'
log_level = 'info'
timeout = 300
