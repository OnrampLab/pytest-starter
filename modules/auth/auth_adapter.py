from injector import inject
import jsonpath
from modules.core import APIClient

class AuthAdapter:
    @inject
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def login(self, email, password):
        responseJson = self.api_client.login(email, password)
        token = jsonpath.jsonpath(responseJson, '$.data')[0]

        return token
