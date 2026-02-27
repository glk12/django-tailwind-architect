web: cd djangoseed && \
	# node steps removed; the buildpack will run `heroku-postbuild`
	# (defined in package.json) during slug compilation. leaving npm
	# in the Procfile caused Railway to select a Node runtime, which
	# does not include python and produced "python: command not found".
	python manage.py migrate --noinput && python manage.py collectstatic --noinput && \
	gunicorn djangoseed.wsgi:application --bind 0.0.0.0:$PORT --log-file -
