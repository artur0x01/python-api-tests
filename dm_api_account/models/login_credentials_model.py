from typing import Optional
from pydantic import BaseModel, Extra, StrictStr, Field


class LoginCredentialsModel(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    remember_me: Optional[bool] = Field(None, alias='rememberMe')
