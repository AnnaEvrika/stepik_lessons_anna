import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-GB',
                      help='Choose GUI language for tests')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language not in ["ru", 'en-GB', 'es', 'fr']:
        raise pytest.UsageError("The wrong language is selected on the page")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart browser for test..")

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    browser.implicitly_wait(7)
    browser.user_language = language

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
    else:
        print("The wrong browser_name is selected in the test")

    yield browser

    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('Screenshots/screenshot-%s.png' % now)
    browser.quit()
