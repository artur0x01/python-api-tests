from typing import Optional
from pydantic import BaseModel, Extra, StrictStr, Field


class ChangeEmailModel(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='User login')
    password: Optional[StrictStr] = Field(None, description='User password')
    email: Optional[StrictStr] = Field(None, description='New user email')
