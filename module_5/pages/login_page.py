from .base_page import BasePage
from .locators import LoginPageLocators
from .data import Links


class LoginPage(BasePage):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.login_page_link
        self.browser.implicitly_wait(timeout)

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.button_login_locator).click()
        email_input = self.browser.find_element(*LoginPageLocators.place_registration_email_locator)
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.place_password_registration_locator)
        password_input.clear()
        password_input.send_keys(password)
        password_input = self.browser.find_element(*LoginPageLocators.place_password_repead_locator)
        password_input.clear()
        password_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.button_registration_locator).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "Incorrect url for registration page"

    def should_be_login_form(self):
        assert self.check_element_is_present(*LoginPageLocators.form_login), "Login form is not presented"

    def should_be_register_form(self):
        assert self.check_element_is_present(*LoginPageLocators.form_register), "Register form is not presented"
