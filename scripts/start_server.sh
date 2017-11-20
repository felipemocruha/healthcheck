until ping -c1 redis &>/dev/null; do :; done
rq worker -u redis://redis:6379 &
rqscheduler --host redis --port 6379 &
gunicorn -b 0.0.0.0:$API_PORT -c gunicorn_conf.py run:app
