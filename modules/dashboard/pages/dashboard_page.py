from modules.admin import AdminLayout


class DashboardPage(AdminLayout):
    XPATH_TITLE = (
        '//main[contains(@class, "ant-layout-content")]//*[contains(text(), "Welcome")]'
    )

    def wait_for_ready(self):
        super().wait_for_ready()

        self.find_global_dom_element_by_xpath(self.XPATH_TITLE)
