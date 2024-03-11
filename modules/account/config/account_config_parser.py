from injector import inject

from interstellar.framework import ConfigService

from .account_config import AccountConfig


class AccountConfigParser:
    @inject
    def __init__(self, config_service: ConfigService):
        self.config = config_service.config

    def get_report_account(self):
        return AccountConfig(self.config["accounts"]["report"])

    def get_empty_shell_account(self):
        return AccountConfig(self.config["accounts"]["empty_shell"])
