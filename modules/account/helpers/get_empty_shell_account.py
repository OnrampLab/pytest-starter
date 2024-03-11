from ..config import AccountConfigParser


def get_empty_shell_account(injector):
    auth_config_parser: AccountConfigParser = injector.get(AccountConfigParser)

    return auth_config_parser.get_empty_shell_account()
