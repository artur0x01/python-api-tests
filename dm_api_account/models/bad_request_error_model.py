from __future__ import annotations
from pydantic import BaseModel, Extra, StrictStr, Field
from typing import Any, Dict, List, Optional


class BadRequestError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')
    invalid_properties: Optional[Dict[str, List[StrictStr]]] = Field(
        None,
        alias='invalidProperties',
        description='Key-value pairs of invalid request properties',
    )
