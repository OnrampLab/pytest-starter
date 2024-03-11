from injector import inject

from interstellar.framework import ConfigService


class AuthConfig:
    @inject
    def __init__(self, config_service: ConfigService):
        self.config = config_service.config

    def get_sys_admin_email(self):
        return self.config["users"]["sys_admin"][0]["email"]

    def get_sys_admin_password(self):
        return self.config["users"]["sys_admin"][0]["password"]
