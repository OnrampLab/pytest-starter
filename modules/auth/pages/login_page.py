from typing import Union

from typing_extensions import Self

from interstellar.framework import MainConfig
from interstellar_antd import Page
from modules.dashboard import DashboardPage


class LoginPage(Page):
    XPATH_EMAIL_INPUT = '//input[@id="email"]'
    XPATH_PASSWORD_INPUT = '//input[@id="password"]'
    XPATH_LOGIN_BUTTON = '//button[@type="submit"]'

    status = "init"

    def login(self, email: str, password: str) -> Union[Self, DashboardPage]:
        main_config = self.injector.get(MainConfig)
        self.driver.get(main_config.get_api_url())

        username_input = self.find_dom_element_by_xpath(self.XPATH_EMAIL_INPUT)
        password_input = self.find_dom_element_by_xpath(self.XPATH_PASSWORD_INPUT)
        login_button = self.find_dom_element_by_xpath(self.XPATH_LOGIN_BUTTON)

        username_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

        message = self.get_ant_message()

        self.logger.info(f"login result message: {message}")

        if "Unauthenticated." in message or "The token has been blacklisted" in message:
            self.status = "failed"
            return self
        elif "Sign complete." in message:
            self.status = "success"
            return self.get_page(DashboardPage)
        else:
            self.status = "unknown"
            self.logger.warn(f"unknown login result message: {message}")
            return self
