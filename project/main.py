from project import create_app

app = create_app()
celery = app.celery_app


@app.on_event("startup")
async def startup_event():
    print("Application started!")
