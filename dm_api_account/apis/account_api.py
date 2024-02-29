from requests import Response
from dm_api_account.models.change_email_model import ChangeEmailModel
from dm_api_account.models.change_password_model import ChangePasswordModel
from dm_api_account.models.registration_model import RegistrationModel
from dm_api_account.models.reset_password_model import ResetPasswordModel
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from restclient.restclient import RestClient


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        self.client.headers = headers
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """

        response = self.client.post(
            path="/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def get_v1_account(self, **kwargs):
        """
        Get current user
        :return:
        """

        response = self.client.get(
            path="/v1/account",
            **kwargs
        )
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        :param token: str
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def post_v1_account_password(self, json: ResetPasswordModel, **kwargs) -> Response:
        """
        :param json reset_password_model
        Reset registered user password
        :return:
        """

        response = self.client.post(
            path="/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        ResetPasswordModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePasswordModel, **kwargs) -> Response:
        """
        :param json change_password_model
        Change registered user password
        :return:
        """

        response = self.client.put(
            path="/v1/account/password",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        ChangePasswordModel(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        param json change_email
        Change registered user email
        :return:
        """

        response = self.client.put(
            path="/v1/account/email",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response
