from .pages.main_page import MainPage
from .pages.login_page import LoginPage


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
        page.go_to_login_page()
        login_page = LoginPage(browser)

        # Assert
        login_page.should_be_login_page()

    # def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
    #     # Arrange
    #     page = MainPage(browser)
    #     page.open()
    #
    #     # Act
    #     page.go_to_basket_page()
    #     basket_page = BasketPage(browser)
    #
    #     # Assert
    #     basket_page.should_not_be_product_in_basket()
    #     basket_page.should_be_empty_basket_message()


#@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser)

        # Assert
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        # Arrange
        page = MainPage(browser)
        page.open()

        # Assert
        page.should_be_login_link()
