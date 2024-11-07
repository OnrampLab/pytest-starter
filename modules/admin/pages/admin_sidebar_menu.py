from transstellar_antd.v5 import Menu, Page


class AdminSidebarMenu(Page):
    XPATH_CURRENT = '//aside[contains(@class, "ant-layout-sider")]'

    def go_to_app_integration_list_page(self) -> Page:
        # Waiting for successful login result page
        menu = self.find_element(Menu)
        menu.select("App Integrations")

        return self.app.get_page("app_integration_list_page")
