from transstellar_antd.v5 import Message, Page, Select

from modules.account import Account
from modules.core import LoadingPage


class AdminHeader(Page):
    XPATH_CURRENT = '//header[contains(@class, "ant-layout-header")]'
    XPATH_AVATAR_IMAGE = '//*[@src="/static/images/avatar.jpg"]'
    # pylint: disable-next=C0301
    XPATH_SIGNOUT_BUTTON = '//span[contains(@class, "ant-dropdown-menu-title-content")]//*[text()="Log Out"]'

    def wait_for_ready(self):
        self.find_global_dom_element_by_xpath(self.XPATH_CURRENT)

    def logout(self):
        self.logger.info("Logging out")

        img_element = self.find_global_dom_element_by_xpath(self.XPATH_AVATAR_IMAGE)
        img_element.click()

        signout_element = self.find_global_dom_element_by_xpath(
            self.XPATH_SIGNOUT_BUTTON
        )

        signout_element.click()

        loading_page = LoadingPage(self.app)
        loading_page.wait_for_ready()

        try:
            loading_page.wait_for_disappear()
            current_path = self.app.get_current_url().path

            assert current_path == "/auth/signin", f"actual path: {current_path}"
        except RuntimeError:
            # TODO: can remove when log out issue is fixed
            self.logger.info("Too long to log out")

        login_page = self.app.go_to("login")

        self.logger.info("Logged out")

        return login_page

    def switch_account(self, account: Account):
        self.logger.info(f"Switching account: {account.name}")

        account_label = f"{account.id} | {account.name}"

        # TODO: it's better to give it an ID to the select

        select = self.find_element(Select)

        if select.get_current_item_title() == account_label:
            self.logger.info(f"Account is already {account_label}")
            return

        select.select_by_search(account_label)

        ant_message: Message = self.find_global_element(Message)

        self.logger.info(f"Message: {ant_message.get_content()}")
