from fastapi import FastAPI

from project.app.celery.celery_utils import create_celery


def create_app() -> FastAPI:
    app = FastAPI()

    from project.app.api import fraud_router

    app.celery_app = create_celery()

    app.include_router(fraud_router)

    return app
