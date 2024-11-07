from transstellar.framework import Module, Route

from modules.auth.pages.login_page import LoginPage

from .auth_adapter import AuthAdapter
from .auth_config_parser import AuthConfigParser
from .entities.user import User


class AuthModule(Module):
    SYSTEM_ADMIN = "system_admin"
    ACCOUNT_ADMIN = "account_admin"
    ACCOUNT_ANALYST = "account_analyst"

    auth_config_parser: AuthConfigParser = None
    system_admin_token: str = None
    system_admin: User = None
    account_admin: User = None
    account_analyst: User = None

    def bootstrap(self):
        self.auth_config_parser = self.app.get(AuthConfigParser)
        self.app.register_routes(
            [
                Route("/", "login", LoginPage),
            ]
        )

    def get_system_admin_token(self):
        if self.system_admin_token:
            return self.system_admin_token

        self.system_admin_token = self.__login_as_system_admin__()

        return self.system_admin_token

    def get_system_admin(self) -> User:
        if self.system_admin:
            return self.system_admin

        self.system_admin = self.auth_config_parser.get_system_admin()

        return self.system_admin

    def get_account_admin(self) -> User:
        if self.account_admin:
            return self.account_admin

        self.account_admin = self.auth_config_parser.get_account_admin()

        return self.account_admin

    def get_account_analyst(self) -> User:
        if self.account_analyst:
            return self.account_analyst

        self.account_analyst = self.auth_config_parser.get_account_analyst()

        return self.account_analyst

    def get_user_by_role(self, role):
        match role:
            case self.SYSTEM_ADMIN:
                return self.get_system_admin()
            case self.ACCOUNT_ADMIN:
                return self.get_account_admin()
            case self.ACCOUNT_ANALYST:
                return self.get_account_analyst()

    def __login_as_system_admin__(self):
        auth_adapter: AuthAdapter = self.app.container.get(AuthAdapter)
        system_admin = self.get_system_admin()

        response = auth_adapter.login(system_admin.email, system_admin.password)

        return response["access_token"]
