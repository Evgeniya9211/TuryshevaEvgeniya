from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class FinanceOzonPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    open_ozon_account = WebElement(xpath='//section[@data-testid="sign-up-section"]//\
                        div[contains(text(), "Открыть")]')
