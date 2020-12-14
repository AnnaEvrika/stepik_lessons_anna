from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка URL на корректность
        assert ('http://selenium1py.pythonanywhere.com/' and 'accounts/login/') in self.browser.current_url, \
            "Incorrect URL"

    def should_be_login_form(self):
        # проверка наличия формы авторизации
        assert self.check_element_is_present(*LoginPageLocators.place_email_address_locator), "Invalid email address"
        assert self.check_element_is_present(*LoginPageLocators.place_password_locator), "Incorrect password"
        assert self.check_element_is_present(*LoginPageLocators.button_login_locator), "Incorrect button"

    def should_be_register_form(self):
        # проверка наличия формы регистрации
        assert self.check_element_is_present(*LoginPageLocators.place_registration_email_locator), "Invalid email address"
        assert self.check_element_is_present(*LoginPageLocators.place_password_locator), "Incorrect password"
        assert self.check_element_is_present(*LoginPageLocators.place_password_repead_locator), "Incorrect password"
        assert self.check_element_is_present(*LoginPageLocators.button_registration_locator), "Incorrect button"
