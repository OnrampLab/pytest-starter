from modules.account.entities.account import Account
from modules.core import Adapter


class AccountAdapter(Adapter):
    def list_accounts(self, params=None):
        self.logger.info("Listing accounts")

        if params is None:
            params = {}

        response_json = self.api_client.account.list(params)

        accounts = self.parse_response(response_json)

        return list(map(lambda data: Account(**data), accounts))
