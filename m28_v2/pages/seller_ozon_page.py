from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class OzonSellerPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    place_for_any_business_on_ozon = WebElement(xpath='//h1[contains(text(), "Любому бизнесу найдётся место на")]')
