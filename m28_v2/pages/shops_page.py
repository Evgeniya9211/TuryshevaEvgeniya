from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class ShopsPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    def get_books(self):
        return self._web_driver.find_elements_by_xpath("//*[contains(text(), 'Книги')]")
