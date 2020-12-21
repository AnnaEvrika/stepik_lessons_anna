from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_login_url()
        self.should_be_add_btn()
        self.add_to_basket()
        self.should_not_be_success_message()
        self.disappear_of_success_message()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert "?promo=newYear" in self.browser.current_url, "String '?promo=newYear' is not in current url of browser"
        assert True

    def should_be_add_btn(self):
        # проверка, что есть кнопка добавленияв корзину
        add_basket = self.is_element_present(*ProductPageLocators.button_add_basket)
        assert self.is_element_present(*ProductPageLocators.button_add_basket), "Button is not presented"
        assert True

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.button_add_basket)
        basket_btn.click()
        assert True


    def check_add_to_basket_notification(self, expected_product_name, expected_notification_template):
        expected_notification_text = expected_notification_template.format(expected_product_name)
        actual_notification_text = self.browser.find_element(By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner").text
        print("Actual product name is " + actual_notification_text, "Expected product name is " + expected_notification_text)
        assert actual_notification_text == expected_notification_text

    def check_product_and_basket_price(self, expected_product_price):
        actual_product_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner>p>strong").text
        print("Actual product price is " + actual_product_price, "Expected product price is " + expected_product_price)
        assert actual_product_price == expected_product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't disappear"