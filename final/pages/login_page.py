from .base_page import BasePage
from final.data.locators import LoginPageLocators, BasePageLocators, UserPageLocators
from final.data.data import Links


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

    def login_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.button_login_locator).click()
        email_login_input = self.browser.find_element(*LoginPageLocators.place_email_address_locator)
        email_login_input.clear()
        email_login_input.send_keys(email)
        password_login_input = self.browser.find_element(*LoginPageLocators.place_password_locator)
        password_login_input.clear()
        password_login_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.button_login_locator).click()

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

    def check_welcome_message(self):
        assert self.check_element_is_present(*UserPageLocators.welcome_message), \
            "User icon is not presented, probably unauthorised user"

    def check_account_button(self):
        assert self.check_element_is_present(*BasePageLocators.user_icon), \
            "Account button is not presented, probably unauthorised user"

    def check_logout_button(self):
        assert self.check_element_is_present(*BasePageLocators.icon_signout), \
            "Logout button is not presented, probably unauthorised user"
