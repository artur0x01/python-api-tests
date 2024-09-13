import time
import structlog
from dm_api_account.models.registration_model import Registration
from services.dm_api_account import DmApiAccount
from services.mailhog import MailHogApi
from dm_api_account.models.user_envelope_model import UserRole
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    #mailhog = MailHogApi(host="http://5.63.153.31:5025")
    #json = Registration(
    #    login="login42",
    #    email="email42@ru",
    #    password="password42"
    #)
    #api.account.post_v1_account(json=json)
    #time.sleep(2)
    #token = mailhog.get_token_from_the_last_email()
    response = api.account.put_v1_account_token(token="a4aa42ee-2f4e-4b55-a05f-135011d81cbe", status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "login42",
            "roles": [UserRole.guest, UserRole.player]
         }
    ))
    #assert response.status_code == 200, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'
