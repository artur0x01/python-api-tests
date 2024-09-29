import time

import structlog
from services.dm_api_account import Facade
from tests.test_post_v1_account_login import test_post_v1_account_login

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade("http://5.63.153.31:5051")
    test_post_v1_account_login()
    time.sleep(2)
    token = api.login.get_auth_token(login='login_test000025', password='password01')

    api.account.set_headers(headers=token)

    api.account.get_current_user_info()