# Скрипт можно запустить из корня проекта командой python module3\test_sample.py, скрипт запускается и проходит без \
# ошибок и исключений; если тест не запускается или падает, оценка за остальные критерии уменьшается в 2 раза
# Структура теста должна выглядеть следующим образом
#1. Предусловия и настройка окружения (открытие браузера, установка дополнительных параметров);
#2. Сами шаги теста;
#3. Проверка на ожидаемый результат: например, на странице находится нужный текст или отображается соответствующий \
# элемент (а может, мы просто убеждаемся, что перешли на корректный URL, - все зависит от того, как вы описывали свои тесты);
#4. Пост-условия: например, закрытие браузера.
# Скрипт описан в виде функции; название тестовой функции соответствует шагам и проверкам в ее теле
# Скрипт использует концепцию ААА: блоки Arrange, Act, Assert визуально отделены друг от друга, содержимое блоков соответствует их названиям
# Названия используемых переменных соответствуют их содержимому
# Скрипт не содержит неиспользуемых переменных
# Скрипт не содержит захардкоженных значений (либо должно быть пояснение, почему хардкод уместен в данном случае)
# assert'ы содержат понятные и подробные сообщения о совершаемой проверке и ожидаемом результат

from selenium import webdriver
import time

main_page_link = "http://selenium1py.pythonanywhere.com//en-gb/"

#локаторы
button_login_or_register_locator = "#login_link"
place_email_address_locator = "#id_login-username.form-control"
place_password_locator = "#id_login-password.form-control"
button_log_in_locator = "#login_form > button"
button_account_locator = "//*[normalize-space(text())='Account']" # (by.xpath("//*[normalize-space(text())='Карты']"))
button_logout_locator = "//*[normalize-space(text())='Logout']"
welcome_title_locator = "//*[normalize-space(text())='Welcome back']"

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
        assert welcome_title in welcome_title.text, \
            "The page contains a greeting"

        button_account = browser.find_element_by_xpath(button_account_locator)
        assert button_account in button_account.text, \
            "The page header must contain the name of the button_account"

        button_logout = browser.find_element_by_xpath(button_logout_locator)
        assert button_logout in button_logout.text, \
            "The page header must contain the name of the button_logout"

    finally:
        time.sleep(5)
        browser.quit()


test_login()

