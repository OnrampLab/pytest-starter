import pytest
from transstellar.framework import BaseApiTest as ParentBaseApiTest


class BaseApiTest(ParentBaseApiTest):
    @pytest.fixture(autouse=True)
    def setup_method_project_base_ui(self):
        pass
