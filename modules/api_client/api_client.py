from transstellar.api_client import APIClient as BaseAPIClient

from .account_api_resource import AccountAPIResource
from .auth_api_resource import AuthAPIResource


class APIClient(BaseAPIClient):
    def __init__(self, base_url: str, options=None):
        super().__init__(base_url, options)

        self.auth: AuthAPIResource = AuthAPIResource(self)
        self.account: AccountAPIResource = AccountAPIResource(self)
