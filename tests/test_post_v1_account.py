import time
from services.dm_api_account import DmApiAccount
import structlog
from services.mailhog import MailHogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailHogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "loginn25",
        "email": "login25@mail.ru",
        "password": "password21"
    }
    # check_input_json(json=json)
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'
    time.sleep(2)
    token = mailhog.get_token_from_the_last_email()
    api.account.put_v1_account_token(token=token)

    # def check_input_json(json):
    for key, value in json.items():
        if key == 'login':
            assert isinstance(value,
                              str), f'Тип значения в ключе {key}, должен быть str, но получен класс {type(value)}'
        elif key == 'email':
            assert isinstance(value,
                              str), f'Тип значения в ключе {key}, должен быть str, но получен класс {type(value)}'
        elif key == 'password':
            assert isinstance(value,
                              str), f'Тип значения в ключе {key}, должен быть str, но получен класс {type(value)}'
