import time
from dm_api_account.models.registration_model import RegistrationModel
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
    json = RegistrationModel(
        login="login3666",
        email="email3666@ru",
        password="password35"
    )
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'
    time.sleep(2)
    token = mailhog.get_token_from_the_last_email()
    api.account.put_v1_account_token(token=token)
