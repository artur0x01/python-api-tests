import time
import structlog
from hamcrest import assert_that, has_properties
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade("http://5.63.153.31:5051")

    login = 'login_test000035'
    email = 'login_test000035@gmail.com'
    password = 'password01'

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    time.sleep(2)

    token = api.login.get_auth_token(
        login=login,
        password=password
    )

    api.account.set_headers(
        headers=token
    )

    response = api.account.get_current_user_info()


    assert_that(response.resource, has_properties(
        {
            "icq": "123",
            "login": "login45"
        }
    ))
