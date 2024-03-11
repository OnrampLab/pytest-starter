from urllib.parse import urlparse

from interstellar_antd import Message, Page, Select

from modules.account import AccountConfig


class AdminHeader(Page):
    XPATH_CURRENT = '//header[@class="ant-layout-header"]'
    XPATH_AVATAR_IMAGE = '//*[@src="/static/images/avatar.jpg"]'
    XPATH_SIGNOUT_BUTTON = '//span[text()="Sign out"]'

    def logout(self):
        self.logger.info("logging out")

        img_element = self.find_dom_element_by_xpath(self.XPATH_AVATAR_IMAGE)
        img_element.click()

        signout_element = self.find_global_dom_element_by_xpath(
            self.XPATH_SIGNOUT_BUTTON
        )
        signout_element.click()

        self.wait_for_dom_element_to_disappear_by_xpath(self.XPATH_SIGNOUT_BUTTON)

        current_path = self.get_current_url().path

        assert current_path == "/", f"actual path: {current_path}"

        self.logger.info("logged out")

    def switch_account(self, account: AccountConfig):
        self.logger.info(f"switching account: {account.get_name()}")

        account_label = f"{account.get_name()} (ID: {account.get_id()})"

        # TODO: it's better to give it an ID to the select
        self.find_element(Select).select(account_label)

        ant_message: Message = self.find_global_element(Message)

        self.logger.info(f"message: {ant_message.get_content()}")
