#!/bin/sh
echo "Waiting for postgres..."

while ! nc -z db 5432; do
    sleep 0.1
done

echo 'Starting Flask Web Application...'
alembic upgrade head
echo "Database Done"
uvicorn project.main:app --reload --workers 1