import time


class Links():
    main_page_link = "http://selenium1py.pythonanywhere.com/"
    login_page_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    basket_page_link = "http://selenium1py.pythonanywhere.com/basket/"
    product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


class User():
    user_email = "testuser_456@123.com"
    user_password = "qazxswedc123"
    registration_repead_email = "testuser_87412565@mail654.com"
    user_fail_email = "fail123564"

class NewUser():
    registration_email = str(time.time()) + "@mailforspam.org"

