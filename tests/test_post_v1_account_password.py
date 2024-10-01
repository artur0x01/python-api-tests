from services.dm_api_account import Facade


def test_post_v1_account_password(login, email):
    api = Facade(host="http://5.63.153.31:5051")


    login = 'login_test000035',
    email = 'login_test000035@gmail.com',
    password = 'password01'

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    api.account_api.post_v1_account_password(
        login = login,
        email = email
    )