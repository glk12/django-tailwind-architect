web: cd djangoseed && \
	# install/build frontend assets before running Django so the generated
	# CSS includes every utility used in our templates (Railway doesn't run
	# `npm run watch:css` automatically).
	npm ci && npm run build:css && \
	python manage.py migrate --noinput && python manage.py collectstatic --noinput && \
	gunicorn djangoseed.wsgi:application --bind 0.0.0.0:$PORT --log-file -
