from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.button_login_locator
        login_link.click()
