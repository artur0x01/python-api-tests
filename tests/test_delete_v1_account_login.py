from services.dm_api_account import DmApiAccount


def test_delete_v1_account_login():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    response = api.login.delete_v1_account_login()
    print(response)
