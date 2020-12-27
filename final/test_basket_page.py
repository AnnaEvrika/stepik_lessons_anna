import pytest

from .pages.product_page import ProductPage


class TestProductPage:
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/",
                              "http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/",
                              "http://selenium1py.pythonanywhere.com/en-gb/catalogue/studyguide-for-counter-hack-reloaded_205/"
                              ])
    def test_guest_can_add_product_to_basket(self, browser, link):

        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_to_basket()
        page.go_to_basket_page()
        # Assert
        page.product_name_on_page()
        page.product_price_on_page()
        # After
        page.delete_from_basket()


