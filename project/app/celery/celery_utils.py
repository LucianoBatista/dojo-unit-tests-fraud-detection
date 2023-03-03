import os
import pathlib

from celery import current_app as current_celery_app


class BaseConfig:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent

    DATABASE_URL: str = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3"
    )
    DATABASE_CONNECT_DICT: dict = {}

    CELERY_BROKER_URL: str = os.environ.get("BROKER_URL", "redis://127.0.0.1:6379/0")
    CELERY_RESULT_BACKEND: str = os.environ.get(
        "RESULT_BACKEND", "redis://127.0.0.1:6379/0"
    )


settings = BaseConfig()


def create_celery():
    celery_app = current_celery_app
    celery_app.config_from_object(settings, namespace="CELERY")

    return celery_app
