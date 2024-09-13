from hamcrest import assert_that, has_properties
from dm_api_account.models.user_details_envelope_model import UserDetails
from services.dm_api_account import DmApiAccount


def test_get_v1_account():
    api = DmApiAccount("http://5.63.153.31:5051")
    response = api.account.get_v1_account(status_code=200)
    assert_that(response.resource, has_properties(
        {
            "icq": "123",
            "login": "login45"
        }
    ))
