from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class TopFashionPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    top_fashion = WebElement(xpath='//h1[contains(text(), "TOP Fashion")]')


