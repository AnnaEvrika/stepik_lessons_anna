from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


# user_language = 'ru', 'en-GB', 'es', 'fr'
# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
# browser = webdriver.Chrome(options=options)

def pytest_add_option(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser language: 'ru', 'en-GB', 'es', 'fr'")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('pref', {'intl.accept_languages': user_language})
    if user_language == "ru":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "en-GB":
        print("\nstart firefox browser for test..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "es":
        print("\nstart firefox browser for test..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "fr":
        print("\nstart firefox browser for test..")
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("browser language must be in range of: 'ru', 'en-GB', 'es', 'fr'")
    yield browser
    browser.quit()
