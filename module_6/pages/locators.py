from selenium.webdriver.common.by import By


class MainPageLocators:
    link_Main_page_locator = "http://selenium1py.pythonanywhere.com/"
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

