from datetime import datetime
from typing import List, Optional

from sqlmodel import DateTime, Field, Relationship, SQLModel


class Model(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    modelname: str
    precision: float
    recall: float
    accuracy: float
    auc: float
    f1: float
    time: float
    enabled: bool
    predicts: List["Predict"] = Relationship(back_populates="model")


class Predict(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    transaction: str
    prediction: bool
    model_id: int = Field(default=None, foreign_key="model.id")
    model: Model = Relationship(back_populates="predicts")


class TrainingQueue(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    dataset: str
    status: str = Field(default="pending")
