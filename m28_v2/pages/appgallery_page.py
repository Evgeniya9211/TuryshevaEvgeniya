from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class AppGalleryPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    ozon_site_link = WebElement(xpath='//div[contains(text(), "OZON: товары, авиа, ж/д билеты")]')
