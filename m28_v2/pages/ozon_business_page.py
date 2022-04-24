from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class OzonBusinessPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    everything_for_your_business_on_ozon = WebElement(xpath='//div[contains(text(), "Всё для вашего ")]')
