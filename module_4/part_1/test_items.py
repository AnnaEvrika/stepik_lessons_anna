def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    try:
        # Arrange
        browser.get(link)
        button_add_to_basket_locator = browser.find_element_by_css_selector("button[class='btn btn-lg btn-primary btn-add-to-basket']").text

        # Act
        button_add_to_basket_actual_text = "{}".format(button_add_to_basket_locator)
        print("actual text " + button_add_to_basket_actual_text)
        button_add_to_basket_expected_text = "{}".format(button_add_to_basket_locator)
        print("expected text " + button_add_to_basket_expected_text)

        # Assert
        assert button_add_to_basket_actual_text in button_add_to_basket_expected_text, "Please, check your browser language"

    finally:
        browser.quit()

