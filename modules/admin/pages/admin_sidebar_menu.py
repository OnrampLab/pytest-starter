from urllib.parse import urlparse

from interstellar_antd import Page


class AdminSidebarMenu(Page):
    XPATH_CURRENT = '//aside[contains(@class, "ant-layout-sider")]'
    XPATH_APP_INTEGRATION = '//*[contains(@class, "ant-menu-item")]/span/a/span[contains(text(), "App Integrations")]/ancestor::a'

    def go_to_app_integration_list_page(self) -> Page:
        # Waiting for successful login result page
        menu = self.find_dom_element_by_xpath(self.XPATH_APP_INTEGRATION)
        menu.click()

        return self.get_page_from_module(
            "modules.app_integration", "AppIntegrationListPage"
        )
