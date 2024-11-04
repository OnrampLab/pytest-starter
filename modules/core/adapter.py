import jsonpath
from injector import inject
from transstellar.framework import Loggable

from modules.api_client import APIClient


class Adapter(Loggable):
    @inject
    def __init__(self, api_client: APIClient, token: str = None):
        super().__init__()
        self.api_client = api_client
        self.api_client.as_token(token)

    def set_token(self, token: str):
        self.api_client.as_token(token)

    def parse_response(self, response_json):
        return jsonpath.jsonpath(response_json, "$.data")[0]
