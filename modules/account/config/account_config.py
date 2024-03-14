from injector import inject
from transstellar.framework import ConfigService


class AccountConfig:
    @inject
    def __init__(self, account_data: dict):
        self.config = account_data

    def get_id(self) -> int:
        return int(self.config["id"])

    def get_name(self) -> str:
        return self.config["name"]

    def get_api_token(self) -> str:
        return self.config["api_token"]
