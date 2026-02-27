#!/usr/bin/env bash
set -euo pipefail

# Run migrations and collectstatic for Railway (use in Release Command)
python3 djangoseed/manage.py migrate --noinput
python3 djangoseed/manage.py collectstatic --noinput

echo "release: migrate + collectstatic completed"
