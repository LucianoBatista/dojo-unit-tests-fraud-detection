#!/bin/sh
echo "Waiting for postgres..."

: "${GUNICORN_CONF:=gunicorn_conf.py}"
: "${WORKER_CLASS:=uvicorn.workers.UvicornWorker}"
: "${APP_MODULE:=project.main:app}"

while ! nc -z db 5432; do
    sleep 0.1
done


if [ "${APP_NAME}" = 'worker' ]; then
    echo 'Starting Worker'

    celery \
        -A project.main.celery worker \
            -l 'INFO' \
            -c "${WORKER_CONCURRENCY:-1}" \
            -E \
            --without-gossip \
            --without-mingle \
            --without-heartbeat
else
    echo 'Starting FastAPI Web Application...'
    alembic upgrade head
    echo "Database Done"
    exec gunicorn \
        -c "${GUNICORN_CONF}" \
        -w "${GUNICORN_CONCURRENCY:-2}" \
        -k "${WORKER_CLASS}" \
        "${APP_MODULE}"
fi