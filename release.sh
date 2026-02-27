#!/bin/bash

/app/.venv/bin/python djangoseed/manage.py migrate --noinput && \
/app/.venv/bin/python djangoseed/manage.py collectstatic --noinput && \
/app/.venv/bin/gunicorn djangoseed.wsgi:application --bind 0.0.0.0:$PORT --log-file -
