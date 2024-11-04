import pytest
from transstellar.framework import BaseUITest as ParentBaseUITest

from modules.auth import LoginPage
from modules.dashboard import DashboardPage


class BaseUITest(ParentBaseUITest):
    @pytest.fixture(autouse=True)
    def setup_method_project_base_ui(self):
        self.dashboard_page: DashboardPage = None
        self.login_page: LoginPage = self.app.go_to("login")

        if hasattr(self, "prepare"):
            self.prepare()

    def login(self, email: str, password: str):
        return self.login_page.login(email, password)

    def logout(self):
        return self.dashboard_page.logout()
