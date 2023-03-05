from typing import Dict, List, Literal, Optional, Union

from pydantic import BaseModel, StrictInt, StrictStr, validator


class ClientTransaction(BaseModel):
    day_of_month: int
    transaction_type: str
    amount_log: float
    amount_dest_log: float
