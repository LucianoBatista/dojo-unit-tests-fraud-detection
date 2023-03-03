from fastapi import APIRouter

fraud_router = APIRouter(prefix="/fraud_detection", tags=["Fraud Detection"])

from . import fraud_detection, tasks
