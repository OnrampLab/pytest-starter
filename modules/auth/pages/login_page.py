from selenium.common.exceptions import TimeoutException
from transstellar_antd.v5 import Page


class LoginPage(Page):
    XPATH_CURRENT = '//div[text()="Sign In"]/ancestor::body'
    XPATH_TITLE = '//div[text()="Sign In"]'
    XPATH_EMAIL_INPUT = '//input[@id="email"]'
    XPATH_PASSWORD_INPUT = '//input[@id="password"]'
    XPATH_LOGIN_BUTTON = '//button[@type="submit"]'

    status = "init"

    def login(self, email: str, password: str):
        self.logger.info(f"Trying to login with email: {email}")
        # Need to wait for title as ready
        self.find_global_dom_element_by_xpath(self.XPATH_TITLE)

        username_input = self.find_dom_element_by_xpath(self.XPATH_EMAIL_INPUT)
        password_input = self.find_dom_element_by_xpath(self.XPATH_PASSWORD_INPUT)
        login_button = self.find_dom_element_by_xpath(self.XPATH_LOGIN_BUTTON)

        username_input.send_keys(email)
        password_input.send_keys(password)
        login_button.click()

        try:
            message = self.get_ant_message()
        except RuntimeError:
            # it's because of re-login
            message = "Account has been changed"

        if (
            "Incorrect email or password" in message
            or "The token has been blacklisted" in message
        ):
            self.logger.info(message)

            self.status = "failed"
        elif "Account has been changed" in message:
            self.logger.info("Login successfully")

            dashboard_page = self.app.get_page("dashboard")

            return dashboard_page
        else:
            self.status = "unknown"
            self.logger.warn(f"unknown login result message: {message}")

        return self
