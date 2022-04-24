from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class GooglePlayPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    ozon_app_title = WebElement(xpath='//span[contains(text(), "OZON: товары, отели, билеты")]')
