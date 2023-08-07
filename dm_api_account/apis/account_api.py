from requests import Response, session
from dm_api_account.models.change_email_model import change_email
from dm_api_account.models import change_password_model
from dm_api_account.models.registration_model import registration_model
from dm_api_account.models.reset_password_model import reset_password_model
from restclient.restclient import RestClient


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        self.client.headers = headers
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return:
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json,
            **kwargs)

        return response

    def get_v1_account(self, **kwargs):
        """
        Get current user
        :return:
        """
        response = self.client.get(
            path=f"/v1/account",
            **kwargs)

        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        :param token: str
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs)

        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:
        """
        :param json reset_password_model
        Reset registered user password
        :return:
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=json,
            **kwargs)

        return response

    def put_v1_account_password(self, json: change_password_model, **kwargs) -> Response:
        """
        :param json change_password_model
        Change registered user password
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=json,
            **kwargs)

        return response

    def put_v1_account_email(self, json: change_email, **kwargs) -> Response:
        """
        param json change_email
        Change registered user email
        :return:
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=json,
            **kwargs)

        return response
