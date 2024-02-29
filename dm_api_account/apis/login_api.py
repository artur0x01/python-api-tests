from requests import Response
from dm_api_account.models.login_credentials_model import LoginCredentialsModel
from dm_api_account.models.user_envelope_model import UserEnvelopeModel
from restclient.restclient import RestClient


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        self.client.headers = headers
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentialsModel) -> Response:
        """
        :param json login_credentials_model
        Authenticate via credentials
        :return:
        """

        response = self.client.post(
            path="/v1/account/login",
            json=json.model_dump(by_alias=True, exclude_none=True)
        )
        UserEnvelopeModel(**response.json())
        return response

    def delete_v1_account_login(self) -> Response:
        """
        Logout as current user
        :return:
        """

        response = self.client.delete(
            path="/v1/account/login"
        )
        return response

    def delete_v1_account_login_all(self) -> Response:
        """
        Logout from every device
        :return:
        """

        response = self.client.delete(
            path="/v1/account/login/all")
        return response
