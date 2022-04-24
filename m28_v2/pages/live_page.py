from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class LivePage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    header_ozon_live = WebElement(xpath='//div[contains(@style, "ozon-live-logo.svg")]')
