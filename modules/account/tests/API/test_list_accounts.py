import pytest

from modules.account import AccountAdapter, AccountModule
from modules.auth import AuthModule
from tests.base_api_test import BaseApiTest


@pytest.mark.account
class TestListAccounts(BaseApiTest):
    account_module: AccountModule
    auth_module: AuthModule

    @pytest.fixture(autouse=True)
    def setup_test(self):
        self.account_module = self.app.get(AccountModule)
        self.auth_module = self.app.get(AuthModule)
        self.account_adapter: AccountAdapter = self.app.get(AccountAdapter)

        token = self.auth_module.get_system_admin_token()
        self.account_adapter.set_token(token)

    def test_get_account(self):
        accounts = self.account_adapter.list_accounts(
            {},
        )

        assert len(accounts) > 0
