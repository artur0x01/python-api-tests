from services.dm_api_account import Facade


def test_post_v1_account_password(login, email):
    api = Facade(host="http://5.63.153.31:5051")
    json = {
        "login": login,
        "email": email
    }
    response = api.account_api.post_v1_account_password(
        json
    )
    print(response)
