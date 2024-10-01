import time
from generic.helpers import mailhog
from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host="http://5.63.153.31:5051")
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')

    login = 'login_test000035'
    email = 'login_test000035@gmail.com'
    password = 'password01'

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    assert response.status_code == 201, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'

    time.sleep(2)

    token = mailhog.MailhogApi.get_token_from_the_last_email()

    api.account.put_v1_account_token(
        token=token
    )

    api.account.activate_registered_user(
        login=login
    )

    db.activate_user_by_login(
        login=login
    )

    api.login.login_user(
        login=login,
        password=password
    )