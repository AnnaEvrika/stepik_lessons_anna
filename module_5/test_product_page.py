import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.data_language_dictionary import LANGUAGES_DICT
from .pages.data import User


class TestProductPage:

    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"


    @pytest.mark.xfail(reason="Задание: проверка независимости контента, поиск бага")
    def test_guest_can_add_product_to_basket(self, browser, link):
        # Data
        product_name = "Coders at Work"
        template = "{} has been added to your basket."
        basket_total_price = "£19.99"

        # Arrange
        link = f"{link}"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес

        # Act
        page.open()  # открываем страницу
        page.should_be_add_btn()
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.check_add_to_basket_notification(product_name, template)
        page.check_product_and_basket_price(basket_total_price)


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()

        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser)

        # Assert
        basket_page.should_not_be_product_in_basket()
        basket_page.should_be_empty_basket_message()


    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()

        # Act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_not_be_success_message()


    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()

        # Assert
        page.should_not_be_success_message()


    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()

        # Act
        page.add_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_disappeared_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()

        # Act
        page.check_go_to_login_page()
        login_page = LoginPage(browser)

        # Assert
        login_page.should_be_login_page()


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser)
        page.open()
        email = str(time.time()) + "@mailforspam.org"
        page.register_new_user(email, User.user_password)
        page.should_be_authorized_user()
        yield

    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()

        # Assert
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser)
        page.open()
        product_name = page.product_name_on_page()
        product_price = page.product_price_on_page()

        # Act
        page.add_to_basket()
        template_name = LANGUAGES_DICT[page.browser.user_language]['add_to_basket_alert_with_name'].format(product_name)

        # Assert
        page.check_alert_add_to_basket_name(template_name)
        page.check_alert_add_to_basket_price(product_price)
