from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class OKPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    title_of_ok_page = WebElement(xpath='//\
                         title[contains(text(), "OZON | Группа на OK.ru | Вступай, читай, общайся в Одноклассниках!")]')
