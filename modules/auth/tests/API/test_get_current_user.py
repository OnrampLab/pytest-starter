import pytest

from modules.auth import AuthAdapter, AuthModule
from tests.base_api_test import BaseApiTest


@pytest.mark.auth
class TestCurrentUser(BaseApiTest):
    auth_module: AuthModule

    @pytest.fixture(autouse=True)
    def setup_test(self):
        self.auth_module: AuthModule = self.app.get(AuthModule)
        self.auth_adapter: AuthAdapter = self.app.get(AuthAdapter)

        token = self.auth_module.get_system_admin_token()
        self.auth_adapter.set_token(token)

    def test_get_current_user(self):
        system_admin = self.auth_module.get_system_admin()

        user = self.auth_adapter.get_current_user()

        assert user.email == system_admin.email
        assert user.is_system_admin()
