#!/usr/bin/env bash
set -euo pipefail

# Use the python3 command directly from the environment
python3 djangoseed/manage.py migrate --noinput
python3 djangoseed/manage.py collectstatic --noinput

echo "release: migrate + collectstatic completed"
