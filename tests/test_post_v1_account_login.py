import time
import structlog
from hamcrest import assert_that, has_properties

from dm_api_account.models.login_credentials_model import LoginCredentials
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.user_envelope_model import UserRole
from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailHogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = Registration(
        login="login_test2",
        email="login_test2@mail.com",
        password="login_test2"
    )
    api.account.post_v1_account(json=json)
    time.sleep(2)
    token = mailhog.get_token_from_the_last_email()
    api.account.put_v1_account_token(token=token)
    json = LoginCredentials(
        login="login_test2",
        password="login_test2",
        rememberMe=True
    )
    response = api.login.post_v1_account_login(
        json=json,
        status_code = 200
    )
    assert_that(response.resource, has_properties(
        {
            "login": "login_test2",
            "roles": [UserRole.guest, UserRole.player],
            "medium_picture_url": None,
            "small_picture_url": None,
            "status": None
        }
    ))
    #assert response.status_code == 201, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'
