from requests import Response
from ..models import *
from restclient.restclient import RestClient
from ..models.utilities import validate_request_json


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        self.client.headers = headers
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: LoginCredentials) -> Response:
        """
        :param json login_credentials_model
        Authenticate via credentials
        :return:
        """

        response = self.client.post(
            path="/v1/account/login",
            json=validate_request_json(json)
        )
        UserEnvelope(**response.json())
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
