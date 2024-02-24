from pydantic import BaseModel, StrictStr, Field
from enum import Enum

registration_model = {
    "login": "login1",
    "email": "login1@mail.ru",
    "password": "<string>",
    "roles": "manager"
}

class Roles(Enum):
    MANAGER = 'manager'
    USER = 'user'


class RegistrationModel(BaseModel):
    login: StrictStr = Field(default='test')
    email: StrictStr = Field(alias='email', title='email')
    password: StrictStr = Field(min_length='1')


print(RegistrationModel(**registration_model).model_dump_json())
