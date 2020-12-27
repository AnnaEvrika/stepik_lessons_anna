from selenium.webdriver.common.by import By
from .base_page import BasePage
from final.data.locators import ProductPageLocators, BasePageLocators, BasketPageLocators
from ..data.data import Links


class ProductPage(BasePage):

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.url = Links.product_page_link
        #self.browser.implicitly_wait(timeout)

    def should_be_product_page(self):
        self.should_be_login_url()
        self.should_be_add_btn()
        self.add_to_basket()
        self.should_not_be_success_message()
        self.disappear_of_success_message()

    def should_be_login_url(self):
        assert "?promo=newYear" in self.browser.current_url, "String '?promo=newYear' is not in current url of browser"
        assert True

    def should_be_add_btn(self):
        add_basket = self.check_element_is_present(*ProductPageLocators.button_add_basket)
        assert self.check_element_is_present(*ProductPageLocators.button_add_basket), "Button is not presented"
        assert True

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.button_add_basket)
        basket_btn.click()
        assert True

    def delete_from_basket(self):
        remove_button = self.browser.find_element(*BasketPageLocators.remove_link)
        remove_button.click()

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
        assert self.check_element_is_not_present(*ProductPageLocators.success_message), \
            "Success message is presented, but should not be"

    def disappear_of_success_message(self):
        assert self.check_element_is_disappeared(*ProductPageLocators.success_message), \
            "Success message isn't disappear"

    def product_name_on_page(self):
        return self.browser.find_element(*ProductPageLocators.product_name_on_page).text

    def product_price_on_page(self):
        return self.browser.find_element(*ProductPageLocators.product_price_on_page).text

    def check_alert_add_to_basket_name(self, expected_text_with_name):
        alerts_list = self.browser.find_elements(*ProductPageLocators.product_was_added_success_alert)
        assert len(alerts_list) > 0, "Error. Not alerts about basket."
        alerts_text = [x.text.rstrip() for x in alerts_list]
        assert expected_text_with_name in alerts_text, "Wrong name or message about adding in basket."

    def check_alert_add_to_basket_price(self, expected_price):
        alert = self.browser.find_element(*ProductPageLocators.product_was_added_info_alert).text
        assert expected_price in alert, "Wrong price or message about adding in basket."

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.basket_link)
        link.click()
    
    def should_disappeared_success_message(self):
        assert self. check_element_is_disappeared(*ProductPageLocators.product_was_added_success_alert), \
            "Success message is presented, but should not be"

    def should_be_login_link(self):
        assert self.check_element_is_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def click_add_to_basket_btn(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.button_add_basket)
        add_to_basket_btn.click()

