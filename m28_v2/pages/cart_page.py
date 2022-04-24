from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class CartPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    # Drop down list with quantity products
    drop_down_list_quantity = ManyWebElements(xpath='//div[@role="listbox"]')

    # Titles of the products in cart
    products_titles = ManyWebElements(xpath='//div/div/a[contains(@class, "tsBodyM") ]/span[1]')

    # Button - delete selected
    delete_selected_button = WebElement(xpath='//span[contains(text(), "Удалить выбранные")]')

    # Button - Confirmation of deletion of selected products
    confirmation_delete_selected_button = WebElement(xpath='//div[contains(text(), "Удалить товар")]/..//\
                                          span[contains(text(), "Удалить")]')

    # Message - your shopping cart is empty
    cart_empty_message = WebElement(xpath='//div[@data-widget="emptyCart"]/h1[contains(text(), "Корзина пуста")]')
