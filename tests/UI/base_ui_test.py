import pytest
from transstellar.framework import BaseUITest as ParentBaseUITest

from modules.auth import LoginPage
from modules.dashboard import DashboardPage


class BaseUITest(ParentBaseUITest):
    login_page: LoginPage
    dashboard_page: DashboardPage

    @pytest.fixture(autouse=True)
    def setup_method_project_base_ui(self, driver):
        self.driver = driver
        self.login_page = self.get_page(LoginPage)

    def login(self, email: str, password: str):
        return self.login_page.login(email, password)

    def logout(self):
        return self.dashboard_page.logout()
