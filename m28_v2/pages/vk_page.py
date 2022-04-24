from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from selenium.webdriver.common.keys import Keys


class VKPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    # title of main page
    title_of_vk_page = WebElement(xpath='//title[contains(text(), "OZON | ВКонтакте")]')
