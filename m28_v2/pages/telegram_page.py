from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class TelegramPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    title_of_telegram_page = WebElement(xpath='//title[text()="Telegram: Contact @ozonhq"]')