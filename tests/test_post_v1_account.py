from dm_api_account.models import Registration
from services.dm_api_account import DmApiAccount
import structlog
from services.mailhog import MailHogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailHogApi(host="http://5.63.153.31:5025")
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = Registration(
        login="login46",
        email="email46@ru",
        password="password46"
    )
    response = api.account.post_v1_account(json=json)
    #time.sleep(2)
    #token = mailhog.get_token_from_the_last_email()
    #api.account.put_v1_account_token(token=token)
