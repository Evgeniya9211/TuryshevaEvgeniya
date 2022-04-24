from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class GeoPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    ozon_order_pickup_points = WebElement(xpath='//h1[contains(text(), "пункты выдачи заказов OZON")]')
