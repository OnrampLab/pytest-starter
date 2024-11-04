import pytest
from transstellar.framework import handle_error

from modules.auth import AuthConfig, LoginPage
from modules.dashboard import DashboardPage
from tests.base_ui_test import BaseUITest


@pytest.mark.smoke
@pytest.mark.auth
@handle_error()
class TestLogin(BaseUITest):
    def prepare(self):
        self.app.driver.set_window_size(1366, 1080)

    def test_login_successfully(self):
        auth_config = self.app.get(AuthConfig)
        dashboard_page: DashboardPage = self.login(
            auth_config.get_system_admin_email(),
            auth_config.get_system_admin_password(),
        )

        assert isinstance(dashboard_page, DashboardPage)

        dashboard_page.sleep(5)

        dashboard_page.logout()

    def test_failed_to_login(self):
        auth_config = self.app.get(AuthConfig)
        login_page = self.login(auth_config.get_system_admin_email(), "wrong_password")

        assert isinstance(login_page, LoginPage)

        assert login_page.status == "failed"
