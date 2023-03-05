from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session

from project.app.models.fraud_models import Model


def get_model_metrics():
    ...


def save_prediction():
    ...


def save_training_queue():
    ...


def get_training_status():
    ...


async def populate_model_baseline(async_session: AsyncSession):
    model_baseline = Model(
        modelname="baseline",
        precision=0.696,
        recall=0.600,
        time=20,
        accuracy=0.899,
        auc=0.838,
        f1=0.788,
        enabled=True,
    )

    async_session.add(model_baseline)
    await async_session.commit()
    await async_session.refresh(model_baseline)
