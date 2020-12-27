import pytest
from final.pages.main_page import MainPage
from final.pages.login_page import LoginPage


class TestMainPage:
    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()

        # Act
        page.check_go_to_login_page()
        login_page = LoginPage(browser)

        # Assert
        login_page.should_be_login_page()


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()

        # Act
        page.check_go_to_login_page()
        login_page = LoginPage(browser)

        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()

        # Assert
        page.should_be_login_link()

