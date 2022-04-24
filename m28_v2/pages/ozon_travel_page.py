from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class OzonTravelPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    serch_for_cheap_flights = WebElement(xpath='//h1[contains(text(), "Поиск дешёвых авиабилетов")]')
