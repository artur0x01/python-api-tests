import time
from hamcrest import assert_that, has_properties
from services.dm_api_account import Facade
from tests.test_post_v1_account_password import test_post_v1_account_password


def test_put_v1_account_password():
    api = Facade(host="http://5.63.153.31:5051")

    login = 'login_test000041'
    email = 'login_test000041@gmail.com'
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

    api.account.set_headers(headers=token)

    login = login
    email = email

    reset_token = test_post_v1_account_password(
        login=login,
        email=email)

    login = "login_test000041"
    token = reset_token
    oldPassword = "password01"
    newPassword = "new_password01"

    response = api.account_api.put_v1_account_password(
        login = login,
        token = reset_token,
        oldPassword = oldPassword,
        newPassword = newPassword
    )

    assert_that(response.resource, has_properties(
        {
            "login": login,
            "status": None,
            "rating": None
        }
    ))