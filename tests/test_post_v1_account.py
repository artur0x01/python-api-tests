from services.dm_api_account import DmApiAccount
import structlog
from services.mailhog import MailHogApi

structlog.configure(processors=[structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)])

def test_post_v1_account():
    api = DmApiAccount(host="http://localhost:5051")
    json = {
        "login": "login14",
        "email": "login14@mail.ru",
        "password": "<string>"
    }
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус кода ответа должен быть равен 201, но он равен {response.status_code}'
    token = MailHogApi.get_token_from_the_last_email()
    response = api.account.put_v1_account_token(token = token)