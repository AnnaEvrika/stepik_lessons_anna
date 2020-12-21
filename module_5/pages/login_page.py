from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка URL на корректность
        assert "login" in self.browser.current_url, "'login' is not in current url of browser"
        assert True

    def should_be_login_form(self):
        # проверка наличия формы авторизации
        assert self.is_element_present(*LoginPageLocators.form_login), "Login form is not found"
        assert True

    def should_be_register_form(self):
        # проверка наличия формы регистрации
        assert self.is_element_present(*LoginPageLocators.form_register), "Registration form is not found"
        assert True

