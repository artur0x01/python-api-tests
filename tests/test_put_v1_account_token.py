import requests
from services.dm_api_account import DmApiAccount


def put_v1_account_token(token):
    api = DmApiAccount(host="http://localhost:5051")
    response = api.account.put_v1_account_token(
        f"{token}"
    )
    print(response)
