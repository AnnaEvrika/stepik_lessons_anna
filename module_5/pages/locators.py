from selenium.webdriver.common.by import By

class GeneralLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class MainPageLocators:
    link_main_page = "http://selenium1py.pythonanywhere.com/"
    button_login_locator = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    form_login = (By.CSS_SELECTOR, "#login_form")
    place_email_address_locator = (By.CSS_SELECTOR, "[name='login-username']")
    place_password_locator = (By.CSS_SELECTOR, "[name='login-password']")
    button_login_locator = (By.CSS_SELECTOR, '[name="login_submit"]')

    form_register = (By.CSS_SELECTOR, "#register_form")
    place_registration_email_locator = (By.CSS_SELECTOR, '[name="registration-email"]')
    place_password_registration_locator = (By.CSS_SELECTOR, '[name="registration-password1"]')
    place_password_repead_locator = (By.CSS_SELECTOR, '[name="registration-password2"]')
    button_registration_locator = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators:
    link_product_page = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    side_categories = (By.CSS_SELECTOR, ".side_categories")
    link_clothing = (By.PARTIAL_LINK_TEXT, "/catalogue/category/clothing_1/")
    link_books = (By.PARTIAL_LINK_TEXT, "/catalogue/category/books_2/")
    link_fiction = (By.PARTIAL_LINK_TEXT, "/catalogue/category/books/fiction_3/")
    link_computers_in_literature = (By.PARTIAL_LINK_TEXT, "/catalogue/category/books/fiction/computers-in-literature_4/")
    link_non_fiction = (By.PARTIAL_LINK_TEXT, "/catalogue/category/books/non-fiction_5/")
    link_essential_programming = (By.PARTIAL_LINK_TEXT, "b/catalogue/category/books/non-fiction/essential-programming_6/")
    link_hacking = (By.PARTIAL_LINK_TEXT, "/catalogue/category/books/non-fiction/hacking_7/")
    page_header = (By.CSS_SELECTOR, ".page-header")
    link_home_page = (By.PARTIAL_LINK_TEXT, "/en-gb/")
    search_line = (By.CSS_SELECTOR, "#id_q")
    button_view_basket = (By.PARTIAL_LINK_TEXT, "/basket/")
    button_add_basket = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')

class BasePageLocators(GeneralLocators):
    login_link_invalid = (By.CSS_SELECTOR, "#login_link_inc")
    basket_link = (By.CSS_SELECTOR, "div.basket-mini span a.btn.btn-default")
    user_icon = (By.CSS_SELECTOR, ".icon-user")

