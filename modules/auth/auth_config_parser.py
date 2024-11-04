from injector import inject
from transstellar.framework import ConfigService

from .entities.user import User


class AuthConfigParser:
    @inject
    def __init__(self, config_service: ConfigService):
        self.config = config_service.config

    def get_system_admin(self):
        return User(**self.config["users"]["system_admin"])

    def get_account_admin(self):
        return User(**self.config["users"]["account_admin"])

    def get_account_analyst(self):
        return User(**self.config["users"]["account_analyst"])

    def get_client_owner(self):
        return User(**self.config["users"]["client_owner"])

    def get_client_analyst(self):
        return User(**self.config["users"]["client_analyst"])
