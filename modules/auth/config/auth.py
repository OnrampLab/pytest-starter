from injector import inject
from transstellar.framework import ConfigService


class AuthConfig:
    @inject
    def __init__(self, config_service: ConfigService):
        self.config = config_service.config

    def get_system_admin_email(self):
        return self.config["users"]["system_admin"]["email"]

    def get_system_admin_password(self):
        return self.config["users"]["system_admin"]["password"]
