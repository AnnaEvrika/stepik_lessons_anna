from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from final.data.data import User, NewUser
from final.pages.main_page import MainPage
from final.pages.login_page import LoginPage
import time


class TestUserRegister:
    def test_user_register(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()

        # Act
        page.register_new_user(NewUser.registration_email, User.user_password)

        # Assert
        page.check_welcome_message()
        page.check_account_button()
        page.check_logout_button()


    def test_user_login(self, browser):
        # Arrange
        page = LoginPage(browser)
        page.open()

        # Act
        page.login_user(User.user_email, User.user_password)

        # Assert
        page.check_welcome_message()
        page.check_account_button()
        page.check_logout_button()


