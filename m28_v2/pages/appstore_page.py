from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class AppStorePage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    def switch_window(self):
        return self.ozon_site_link.keybord_ctrl_tab()

    ozon_site_link = WebElement(xpath='//a[contains(@href, "apps.apple.com/us/developer/ozon-ru")]')
