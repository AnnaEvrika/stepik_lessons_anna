from selenium.webdriver.common.by import By

button_add_to_basket_dictionary = {
    'ru': 'Добавить в корзину',
    'en-gb': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier'
}


def test_button_add_to_basket(browser):
    # Data
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    button_add_to_basket_locator = '.btn-add-to-basket'
    site_language = browser.user_language
    button_add_to_basket_text = button_add_to_basket_dictionary[site_language]

    # Arrange
    browser.get(link)

    # Act
    button_add_to_basket = browser.find_element(By.CSS_SELECTOR, button_add_to_basket_locator)

    # Assert
    assert button_add_to_basket_text in button_add_to_basket.text, 'Achtung! The text of the button is incorrect'


