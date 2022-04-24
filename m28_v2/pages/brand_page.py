from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class BrandPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    def get_apple(self):
        return self._web_driver.find_element_by_xpath("//a[contains(@href, '/brand/apple')]")
