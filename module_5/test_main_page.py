from module_5.pages.main_page import MainPage


def test_guest_should_see_login_link(self, browser):
    page = MainPage(browser, link_main_page)
    page.open()
    page.should_be_login_link()

