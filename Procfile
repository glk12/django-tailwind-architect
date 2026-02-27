web: cd djangoseed && \
	python manage.py migrate --noinput && python manage.py collectstatic --noinput && \
	gunicorn djangoseed.wsgi:application --bind 0.0.0.0:$PORT --log-file -
