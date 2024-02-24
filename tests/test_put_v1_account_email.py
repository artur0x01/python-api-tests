import time
import structlog
from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailHogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "loginn28",
        "email": "login28@mail.ru",
        "password": "password21"
    }
    # check_input_json(json=json)
    api.account.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_the_last_email()
    api.account.put_v1_account_token(token=token)
    json = {
        "login": "loginn28",
        "email": "login29@mail.ru",
        "password": "password21"
    }
    response = api.account.put_v1_account_email(
        json
    )
    assert response.status_code == 200, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'
