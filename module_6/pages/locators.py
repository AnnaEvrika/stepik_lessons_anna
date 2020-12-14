from selenium.webdriver.common.by import By


class MainPageLocators:
    button_login_or_register_locator = "#login_link"


class LoginPageLocators:
    place_email_address_locator = (By.CSS_SELECTOR, "[name='login-username']")
    place_password_locator = (By.CSS_SELECTOR, "[name='login-password']")
    button_login_locator = (By.CSS_SELECTOR, '[name="login_submit"]')

    place_registration_email_locator = (By.CSS_SELECTOR, '[name="registration-email"]')
    place_password_registration_locator = (By.CSS_SELECTOR, '[name="registration-password1"]')
    place_password_repead_locator = (By.CSS_SELECTOR, '[name="registration-password2"]')
    button_registration_locator = (By.CSS_SELECTOR, '[name="registration_submit"]')

