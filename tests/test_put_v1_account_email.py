import time
import structlog
from hamcrest import has_properties, assert_that
from services.dm_api_account import Facade
from generic.helpers.mailhog import MailHogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailHogApi(host="http://5.63.153.31:5025")
    api = Facade(host="http://5.63.153.31:5051")

    login = 'login_test000035'
    email = 'login_test000035@gmail.com'
    password = 'password01'

    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    time.sleep(2)

    token = mailhog.get_token_from_the_last_email()

    api.account_api.put_v1_account_token(
        token=token
    )

    login = "login48"
    password = "password"
    email = "email49@mail.ru"

    response = api.account_api.put_v1_account_email(
        login=login,
        password = password,
        email = email,
        status_code=200
    )

    assert response.status_code == 200, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'

    assert_that(response.resource, has_properties(
        {
            "login": login,
            "email": email,
            "medium_picture_url": None,
            "small_picture_url": None,
            "status": None,
        }
    )
                )
