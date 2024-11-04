import pytest
from transstellar.api_client import UnauthorizedError

from modules.auth import AuthAdapter, AuthConfig
from tests.base_api_test import BaseApiTest


@pytest.mark.smoke
@pytest.mark.auth
class TestLogin(BaseApiTest):
    auth_adapter: AuthAdapter

    @pytest.fixture(autouse=True)
    def setup_test(self):
        self.auth_adapter = self.app.get(AuthAdapter)

    def test_successful_login(self):
        config = self.app.get(AuthConfig)

        result = self.auth_adapter.login(
            config.get_system_admin_email(), config.get_system_admin_password()
        )

        assert isinstance(result["access_token"], str)
        assert result["token_type"] == "bearer"
        assert result["expires_in"] == 1209600000

    def test_failed_login(self):
        config = self.app.get(AuthConfig)

        try:
            self.auth_adapter.login(config.get_system_admin_email(), "wrong_password")
            assert False
        except UnauthorizedError:
            assert True
