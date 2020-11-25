from selenium import webdriver
from selenium.webdriver.common.by import By
import time

main_page_link = "http://selenium1py.pythonanywhere.com/ru"

# локаторы
button_login_or_register_locator = "#login_link"
place_email_address_locator = "[name='login-username']"
place_password_locator = "[name='login-password']"
button_login_locator = "#login_form > button"
button_account_locator = "//*[normalize-space(text())='Аккаунт']"
button_logout_locator = "//*[normalize-space(text())='Выход']"
welcome_title_locator = "//*[normalize-space(text())='Рады видеть вас снова']"


def test_login():
    # Data
    user_email = "testuser_456@123.com"
    user_password = "qazxswedc123"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        browser.find_element(By.CSS_SELECTOR, button_login_or_register_locator).click()

        # элементы
        place_email_address = browser.find_element(By.CSS_SELECTOR, place_email_address_locator)
        place_password = browser.find_element(By.CSS_SELECTOR, place_password_locator)
        button_login = browser.find_element(By.CSS_SELECTOR, button_login_locator)


        # Act
        place_email_address.send_keys(user_email)
        place_password.send_keys(user_password)
        button_login.click()

        # Assert
        welcome_title = browser.find_element_by_xpath(welcome_title_locator)
        assert welcome_title.is_displayed(), \
            "The page contains a greeting"

        button_account = browser.find_element_by_xpath(button_account_locator)
        assert button_account.is_displayed(), \
            "The page header must contain the name of the button_account"

        button_logout = browser.find_element_by_xpath(button_logout_locator)
        assert button_logout.is_displayed(), \
            "The page header must contain the name of the button_logout"

    finally:
        time.sleep(5)
        browser.quit()

test_login()


