command='root/accel/vdjango/bin/gunicorn'
pythonpath='/root/accel'
bind='89.33.44.114:8000'
workers=2
loglevel = "info"
errorlog = "/root/accel/logs/error.log"
accesslog = "/root/accel/logs/access.log"
