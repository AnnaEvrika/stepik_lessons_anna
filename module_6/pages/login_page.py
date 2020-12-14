from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert ('http://selenium1py.pythonanywhere.com/' and 'accounts/login/') in self.browser.current_url, \
            "Incorrect URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_LINK), "Correct e-mail not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PSD_LINK), "Wrong password"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Incorrect button"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_LINK), "Correct e-mail not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PSD_LINK), "Wrong password"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PSD_REPEAT_LINK), "Wrong password"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PSD_REPEAT_LINK), "Incorrect button"
