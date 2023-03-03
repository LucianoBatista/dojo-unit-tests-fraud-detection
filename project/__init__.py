from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    from project.app.api import fraud_router

    app.include_router(fraud_router)

    return app
