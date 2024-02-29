from pydantic import BaseModel, Extra, StrictStr, Field


class RegistrationModel(BaseModel):
    class Config:
        extra = Extra.forbid

    login: StrictStr = Field(None, description='Login')
    email: StrictStr = Field(None, description='Email')
    password: StrictStr = Field(None, description='Password')
