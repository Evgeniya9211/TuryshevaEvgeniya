from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class BusinessOzonPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    develop_your_business = WebElement(xpath='//h3[contains(text(), "Развивайте бизнес")]')
