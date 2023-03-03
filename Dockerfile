# base official image
FROM python:3.10.0-slim-buster

LABEL maintainer='Luba'

# set working directory
WORKDIR /usr/src/app

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# copying requirements
COPY Pipfile* ./

RUN pip install -q --no-cache-dir \
    pipenv && \
    pipenv install --system

COPY ./ ./

COPY ./entrypoint.sh /sbin/entrypoint.sh
RUN sed -i 's/\r$//g' /sbin/entrypoint.sh
RUN chmod +x /sbin/entrypoint.sh

ENTRYPOINT ["/sbin/entrypoint.sh"]