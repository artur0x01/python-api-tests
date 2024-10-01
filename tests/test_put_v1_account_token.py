import time
import structlog
from generic.helpers.mailhog import MailhogApi
from services.dm_api_account import Facade
from dm_api_account.models.user_envelope_model import UserRole
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host="http://5.63.153.31:5051")
    mailhog = MailhogApi(host="http://5.63.153.31:5025")

    login = 'login_test000040'
    email = 'login_test000040@gmail.com'
    password = 'password01'

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    time.sleep(2)

    token = mailhog.get_token_from_the_last_email()

    response = api.account_api.put_v1_account_token(token=token, status_code=200)

    assert_that(response.resource, has_properties(
        {
            "login": "login42",
            "roles": [UserRole.guest, UserRole.player]
        }
    )
                )

    assert response.status_code == 200, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'

