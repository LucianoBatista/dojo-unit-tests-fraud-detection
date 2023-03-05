import pandas as pd
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session

from project.app.database import crud
from project.app.db import get_session
from project.app.fraud_detection import fraud_router
from project.app.fraud_detection.prediction import predict
from project.app.fraud_detection.tasks import async_workflow
from project.app.schemas.client_transaction import ClientTransaction


@fraud_router.post("/detect")
def fraud_detection(client_transaction: ClientTransaction):
    # data
    data = {
        "day_of_month": client_transaction.day_of_month,
        "type": client_transaction.transaction_type,
        "amount_log": client_transaction.amount_log,
        "amount_dest_log": client_transaction.amount_dest_log,
    }

    data_df = pd.DataFrame(data, index=[0])

    # do the prediction
    predictions = predict(data_df)
    predictions = [int(prediction) for prediction in predictions]

    if predictions[0] == 1:
        return {"prediction": "fraud"}
    elif predictions[0] == 0:
        return {"prediction": "no fraud"}


@fraud_router.post("/model/training")
def train_model(dataset_url: str):
    # start a training process
    return {"processing_id": 123}


@fraud_router.get("/model/training/status")
def check_status(id: int):
    # obj = model_crud.get_status(id)
    return {"status": "Processing"}


@fraud_router.get("/model/health")
def check_health():
    # obj = model_crud.get_metrics()
    response = {
        "modelname": "model",
        "accuracy": 0.3,
        "recall": 0.9,
        "f1": 0.87,
        "enabled": True,
    }
    return response


@fraud_router.post("/poppulate_model")
async def poppulate_model(engine: AsyncSession = Depends(get_session)):
    await crud.populate_model_baseline(engine)
    return {"message": "Model populated"}
