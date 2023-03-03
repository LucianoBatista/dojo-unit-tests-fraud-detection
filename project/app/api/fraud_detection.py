from project.app.api import fraud_router
from project.app.api.tasks import async_workflow


@fraud_router.get("/detect")
def get_content_tree(client_data: str):
    if client_data == "fraudulent":
        return {"message": "Fraudulent client"}
        _ = async_workflow.delay()
    else:
        return {"message": "Not fraudulent client"}


@fraud_router.post("/training")
def train_model():
    return {"message": "Training model"}


@fraud_router.get("/model")
def get_model():
    return {"message": "Model"}
