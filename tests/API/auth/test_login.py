import pytest
from transstellar.api_client import UnauthorizedError
from transstellar.framework import BaseApiTest

from modules.auth import AuthAdapter, AuthConfig


@pytest.mark.smoke
class TestLogin(BaseApiTest):
    auth_adapter: AuthAdapter

    @pytest.fixture(autouse=True)
    def setup_test(self):
        self.auth_adapter = self.injector.get(AuthAdapter)

    def test_successful_login(self):
        config = self.injector.get(AuthConfig)

        result = self.auth_adapter.login(
            config.get_sys_admin_email(), config.get_sys_admin_password()
        )

        assert type(result["access_token"]) == str
        assert result["token_type"] == "bearer"
        assert result["expires_in"] == 86400

    def test_failed_login(self):
        config = self.injector.get(AuthConfig)

        try:
            self.auth_adapter.login(config.get_sys_admin_email(), "wrong_password")
            assert False
        except UnauthorizedError as e:
            assert True
