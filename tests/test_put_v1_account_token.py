import token
from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi


def test_put_v1_account_token():
    api = DmApiAccount(host="http://localhost:5051/")
    result = MailHogApi()
    response = api.account.put_v1_account_token(token)
    return response
