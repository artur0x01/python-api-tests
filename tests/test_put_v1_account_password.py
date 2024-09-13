import requests
from hamcrest import assert_that, has_properties
from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "login46",
        "token": "69eff10a-58d8-409e-b2f3-fc8dada4060e",
        "oldPassword": "password46",
        "newPassword": "new_password46"
    }
    response = api.account.put_v1_account_password(
        json=json,
        status_code=200
    )
    assert_that(response.resource, has_properties(
        {
            "login": "login43",
            "status": None,
            "rating": None
        }
    ))
    print(response)
