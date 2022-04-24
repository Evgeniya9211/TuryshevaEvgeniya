from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class DocsCommon(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    payment_methods = WebElement(xpath='//article//a[@href="/common/oplata/sposoby-oplaty/"]')
