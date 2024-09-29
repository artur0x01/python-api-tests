import time
import requests
from hamcrest import assert_that, has_properties
from services.dm_api_account import Facade
from tests.test_post_v1_account_login import test_post_v1_account_login
from tests.test_post_v1_account_password import test_post_v1_account_password


def test_put_v1_account_password():
    api = Facade(host="http://5.63.153.31:5051")
    test_post_v1_account_login()
    time.sleep(2)
    token = api.login.get_auth_token(login='login_test000029', password='password01')
    api.account.set_headers(headers=token)

    reset_token = test_post_v1_account_password(login='login_test000029', email='login_test000029@gmail.com')

    json = {
        "login": "login_test000029",
        "token": reset_token,
        "oldPassword": "password01",
        "newPassword": "new_password01"
    }

    response = api.account_api.put_v1_account_password(
        json=json,
        status_code=200
    )
