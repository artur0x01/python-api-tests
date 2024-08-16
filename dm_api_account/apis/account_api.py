from requests import Response
from ..models import RegistrationModel
from restclient.restclient import RestClient
from ..models.utilities import validate_request_json


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
        UserEnvelope(**response.json())
        return response

    def post_v1_account_password(self, json: ResetPassword, **kwargs) -> Response:
        """
        :param json reset_password_model
        Reset registered user password
        :return:
        """

        response = self.client.post(
            path="/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        ResetPassword(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePassword, **kwargs) -> Response:
        """
        :param json change_password_model
        Change registered user password
        :return:
        """

        response = self.client.put(
            path="/v1/account/password",
            json=validate_request_json(json),
            **kwargs
        )
        ChangePassword(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmail, **kwargs) -> Response:
        """
        param json change_email
        Change registered user email
        :return:
        """

        response = self.client.put(
            path="/v1/account/email",
            json=validate_request_json(json),
            **kwargs
        )
        UserEnvelope(**response.json())
        return response
