from module_5.pages.base_page import BasePage
from module_5.pages.data import Links
from module_5.pages.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.main_page_link
        self.browser.implicitly_wait(timeout)

    def should_be_login_link(self):
        assert self.check_element_is_present(*MainPageLocators.button_login_locator), "Button login link is not found"

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.button_login_locator)
        link.click()


