import pytest

from modules.auth import AuthConfig, LoginPage
from modules.dashboard import DashboardPage
from tests.UI.base_ui_test import BaseUITest


@pytest.mark.smoke
class TestLogin(BaseUITest):
    def assert_login_failed(self):
        # Waiting for successful login result page
        login_page: LoginPage = self.get_page(LoginPage)
        login_failed_message = login_page.get_ant_message()

        assert "Unauthenticated." in login_failed_message

    def test_login_successfully(self):
        auth_config = self.injector.get(AuthConfig)
        dashboard_page: DashboardPage = self.login(
            auth_config.get_sys_admin_email(), auth_config.get_sys_admin_password()
        )

        assert isinstance(dashboard_page, DashboardPage)

        dashboard_page.logout()

    def test_failed_to_login(self):
        auth_config = self.injector.get(AuthConfig)
        login_page = self.login(auth_config.get_sys_admin_email(), "wrong_password")

        assert isinstance(login_page, LoginPage)

        self.assert_login_failed()
