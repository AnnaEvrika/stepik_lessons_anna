# Скрипт можно запустить из корня проекта командой python module3\test_sample.py, скрипт запускается и проходит без \
# ошибок и исключений; если тест не запускается или падает, оценка за остальные критерии уменьшается в 2 раза

from selene.support.conditions import be
from selenium import webdriver
import time

main_page_link = "http://selenium1py.pythonanywhere.com/ru"

#локаторы
button_login_or_register_locator = "#login_link"
place_email_address_locator = "#id_login-username.form-control"
place_password_locator = "#id_login-password.form-control"
button_log_in_locator = "#login_form > button"
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

        button_login_or_register = browser.find_element_by_css_selector(button_login_or_register_locator)
        button_login_or_register.click()
        browser.implicitly_wait(5)

        place_email_address = browser.find_element_by_css_selector(place_email_address_locator)
        place_password = browser.find_element_by_css_selector(place_password_locator)

        # Act
        place_email_address.send_keys(user_email)
        browser.implicitly_wait(5)
        place_password.send_keys(user_password)
        browser.find_element_by_css_selector(button_log_in_locator).click()

        # Assert
        welcome_title = browser.find_element_by_xpath(welcome_title_locator)
        assert welcome_title(be.visible),\
            "The page contains a greeting"

        button_account = browser.find_element_by_xpath(button_account_locator)
        assert button_account(be.visible),\
            "The page header must contain the name of the button_account"

        button_logout = browser.find_element_by_xpath(button_logout_locator)
        assert button_logout(be.visible),\
            "The page header must contain the name of the button_logout"

    finally:
        time.sleep(5)
        browser.quit()


test_login()

