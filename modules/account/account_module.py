from transstellar.framework.module import Module

from .config.account_config_parser import AccountConfigParser
from .entities.account import Account


class AccountModule(Module):
    EMPTY_SHELL = "empty_shell"
    REPORT = "report"

    auth_config_parser: AccountConfigParser
    empty_shell_account: Account = None
    report_account: Account = None

    def bootstrap(self):
        self.auth_config_parser: AccountConfigParser = self.app.get(AccountConfigParser)

    def get_empty_shell_account(self):
        if self.empty_shell_account:
            return self.empty_shell_account

        self.empty_shell_account = self.auth_config_parser.get_empty_shell_account()

        return self.empty_shell_account

    def get_report_account(self):
        if self.report_account:
            return self.report_account

        self.report_account = self.auth_config_parser.get_report_account()

        return self.report_account

    def get_account_by_name(self, account_name: str):
        match account_name:
            case self.EMPTY_SHELL:
                return self.get_empty_shell_account()
            case self.REPORT:
                return self.get_report_account()
