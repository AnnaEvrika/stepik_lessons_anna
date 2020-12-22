import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_add_option(parser):
    parser.addoption('--language', action='store', default='en-GB',
                     help="Choose browser language: 'ru', 'en-GB', 'es', 'fr'")


# фикстура browser
@pytest.fixture(scope="function")
def browser(request):
    # обработчик опции language
    user_language = request.config.getoption("language")
    options = Options()

    if user_language not in ["ru", "en-GB", "es", "fr"]:
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        raise pytest.UsageError("Achtung! The browser language is incorrect. The browser language must be 'ru', "
                                "'en-GB', 'es', 'fr'")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    # передача языка в объект браузера
    browser.user_language = user_language

    # закрытие браузера после прохождения теста
    yield browser
    browser.quit()

