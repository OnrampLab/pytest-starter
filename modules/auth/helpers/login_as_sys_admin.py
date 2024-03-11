from injector import inject

from modules.auth import AuthConfig
from modules.auth.auth_adapter import AuthAdapter


def login_as_sys_admin(injector):
    auth_adapter: AuthAdapter = injector.get(AuthAdapter)
    config = injector.get(AuthConfig)

    result = auth_adapter.login(
        config.get_sys_admin_email(), config.get_sys_admin_password()
    )

    return result["access_token"]
