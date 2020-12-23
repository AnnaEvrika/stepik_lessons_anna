from module_5.pages.main_page import TestMainPage


def test_guest_should_see_login_link(self, browser):
    page = TestMainPage(browser, link_main_page)
    page.open()
    page.should_be_login_link()

