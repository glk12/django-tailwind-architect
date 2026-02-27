web: bash -lc "python djangoseed/manage.py migrate --noinput && python djangoseed/manage.py collectstatic --noinput && gunicorn djangoseed.wsgi:application --bind 0.0.0.0:$PORT --log-file -"
