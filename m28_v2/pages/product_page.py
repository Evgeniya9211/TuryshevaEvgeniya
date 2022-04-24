from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class ProductPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    def press_plus_symbol_button_n_times(self, number_press):
        for i in range(number_press):
            self.plus_symbol_button.click()
            self.wait_page_loaded()

    def press_minus_symbol_button_n_times(self, number_press):
        for i in range(number_press):
            self.minus_symbol_button.click()
            self.wait_page_loaded()

    def add_in_cart_button_click(self):
        if self.add_in_cart_button.is_presented():
            self.add_in_cart_button.click()
        elif self.div_add_in_cart_button.is_presented():
            self.div_add_in_cart_button.click()
        else:
            self.in_cart_button.click()

    def get_elektronnyy_podarochnyy_sertifikat_million_podarkov(self):
        return self._web_driver.find_element_by_xpath("//h1[text()='ozon Электронный подарочный сертификат Миллион подарков (3000)']")

    # Add product in cart button
    add_in_cart_button = WebElement(xpath='//button/span/span[contains(text(), "Добавить в корзину")]')

    # in cart button
    in_cart_button = WebElement(xpath='//button/span/div/div/div[contains(text(), "В корзину")]')

    div_add_in_cart_button = WebElement(xpath='//div[contains(text(), "Добавить в корзину")]')

    go_to_cart_button = WebElement(xpath='//span[contains(text(), "В корзине")]//span[contains(text(), "Перейти")]')

    #  Plus button on product page (need take 4 list element)
    plus_symbol_button = WebElement(xpath='//div[@data-widget="webAddToCart"]//\
    button/span[contains(@style, "border-radius:")]//*[@clip-rule="evenodd"]')

    minus_symbol_button = WebElement(xpath='//div[@data-widget="webAddToCart"]//\
    button/span[contains(@style, "border-radius:")]//*[@x]')

    # Drop down list with quantity products
    field_quantity_products = ManyWebElements(xpath='//div[@data-widget="webAddToCart"]/div/div/div/div//div/span[2]')
