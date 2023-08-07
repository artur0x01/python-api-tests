import json
import requests
from restclient.restclient import RestClient


class MailHogApi:
    def __init__(self, host="http://localhost:5025"):
        self.host = host
        self.client = RestClient(host=host)

    def get_api_v2_messages(self, limit=50):
        response = self.client.get(
            path=f"/api/v2/messages",
            params={
                "limit": limit
            }
        )

        return response

    def get_token_from_the_last_email(self):
        emails = self.get_api_v2_messages(limit=1).json()
        token = json.loads(emails['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[4]
        return token
