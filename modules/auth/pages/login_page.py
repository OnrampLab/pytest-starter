from typing import Union

from transstellar.framework import MainConfig
from transstellar_antd.v5 import Page
from typing_extensions import Self

from modules.dashboard import DashboardPage


class LoginPage(Page):
    XPATH_EMAIL_INPUT = '//input[@id="email"]'
    XPATH_PASSWORD_INPUT = '//input[@id="password"]'
    XPATH_LOGIN_BUTTON = '//button[@type="submit"]'

    status = "init"

    def login(self, email: str, password: str) -> Union[Self, DashboardPage]:
        main_config = self.injector.get(MainConfig)
        self.driver.get(main_config.get_app_url())

        username_input = self.find_global_dom_element_by_xpath(self.XPATH_EMAIL_INPUT)
        password_input = self.find_global_dom_element_by_xpath(
            self.XPATH_PASSWORD_INPUT
        )
        login_button = self.find_global_dom_element_by_xpath(self.XPATH_LOGIN_BUTTON)

        username_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

        try:
            message = self.get_ant_message()

            if (
                "Incorrect email or password" in message
                or "The token has been blacklisted" in message
            ):
                self.status = "failed"
            else:
                self.status = "unknown"
                self.logger.warn(f"unknown login result message: {message}")

            return self
        except Exception as e:
            dashboard_page: DashboardPage = self.get_page(DashboardPage)
            return dashboard_page
