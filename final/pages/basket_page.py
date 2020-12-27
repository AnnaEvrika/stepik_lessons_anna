from .base_page import BasePage
from final.data.locators import BasketPageLocators
from final.data import Links
from final.data.data_language_dictionary import LANGUAGES_DICT


class BasketPage(BasePage):
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.basket_page_link
        self.browser.implicitly_wait(timeout)

    def should_not_be_product_in_basket(self):
        assert self.check_element_is_not_present(*BasketPageLocators.products_in_basket), \
            "The product is in the basket, but it shouldn't be"

    def should_be_empty_basket_message(self):
        message = self.browser.find_element(*BasketPageLocators.empty_basket_message).text
        assert LANGUAGES_DICT[self.browser.user_language]['empty_basket'] in message, \
            "Empty basket message is not, but should be."
