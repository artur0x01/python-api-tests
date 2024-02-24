from requests import Response
from dm_api_account.models import login_credentials_model
from restclient.restclient import RestClient


class LoginApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = RestClient(host=host, headers=headers)
        self.client.headers = headers
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account_login(self, json: login_credentials_model) -> Response:
        """
        :param json login_credentials_model
        Authenticate via credentials
        :return:
        """

        response = self.client.post(
            path="/v1/account/login",
            json=json
        )
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
