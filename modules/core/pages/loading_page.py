from transstellar_antd.v5 import Page


class LoadingPage(Page):
    # pylint: disable-next=C0301
    XPATH_CURRENT = '//div[contains(@class, "loading-bar-animation")]/ancestor::div[contains(@class, "items-center justify-center")]'

    def wait_for_ready(self):
        self.find_global_dom_element_by_xpath(self.XPATH_CURRENT)

    def wait_for_disappear(self):
        self.wait_for_dom_element_to_disappear_by_xpath(self.XPATH_CURRENT)
