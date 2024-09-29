from dm_api_account.models import Registration
from services.dm_api_account import Facade
import structlog
from generic.helpers.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host="http://5.63.153.31:5025")
    api = Facade(host="http://5.63.153.31:5051")
    json = Registration(
        login="login_test000011",
        email="login_test000011@gmail.com",
        password="password01"
    )
    response = api.account_api.post_v1_account(json=json)
    #time.sleep(2)
    #token = mailhog.get_token_from_the_last_email()
    #api.account.put_v1_account_token(token=token)
