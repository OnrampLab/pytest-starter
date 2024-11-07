from injector import inject
from transstellar.framework import ConfigService

from ..entities.account import Account


class AccountConfigParser:
    @inject
    def __init__(self, config_service: ConfigService):
        self.config = config_service.config

    def get_report_account(self):
        return Account(**self.config["accounts"]["report"])

    def get_empty_shell_account(self):
        return Account(**self.config["accounts"]["empty_shell"])
