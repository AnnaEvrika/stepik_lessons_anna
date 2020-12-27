import pytest
from final.data.data import User, NewUser
from final.pages.login_page import LoginPage


@pytest.mark.login_user
class TestUserLoginRegister:
    def test_user_register(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()

        # Act
        page.register_new_user(NewUser.registration_email, User.user_password)

        # Assert
        page.check_welcome_message()
        page.check_account_button()
        page.check_logout_button()

    def test_user_login(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()

        # Act
        page.login_user(User.user_email, User.user_password)

        # Assert
        page.check_welcome_message()
        page.check_account_button()
        page.check_logout_button()

    def test_user_logout(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()
        page.login_user(User.user_email, User.user_password)

        # Act
        page.logout_user()

        # Assert
        page.check_login_button()

    @pytest.mark.xfail
    def test_user_fail_register(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()

        # Act
        page.register_new_user(User.registration_repead_email, User.user_password)

        # Assert
        page.check_welcome_message()
        page.check_account_button()
        page.check_logout_button()

    @pytest.mark.xfail
    def test_user_fail_login(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()

        # Act
        page.login_user(User.user_fail_email, User.user_password)

        # Assert
        page.check_welcome_message()
        page.check_account_button()
        page.check_logout_button()

