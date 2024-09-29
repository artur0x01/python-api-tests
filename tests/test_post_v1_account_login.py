import time
import structlog
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = Facade(host="http://5.63.153.31:5051")

    login = 'login_test000031'
    email = 'login_test000031@gmail.com'
    password = 'password01'

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    time.sleep(2)

    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password
    )
