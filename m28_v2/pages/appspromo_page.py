from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class AppsPromoPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    def switch_window(self):
        return self.available_in_google_play.keybord_ctrl_tab()

    def get_download_appstore(self):
        return self._web_driver.find_element_by_xpath('//div[@class="apps-color apps-header"]//\
                                                      a[contains(@href, "itunes.apple.com/us/app")]')

    def get_available_in_google_play(self):
        return self._web_driver.find_element_by_xpath('//div[@class="apps-color apps-header"]//\
                                                      a[contains(@href, "play.google.com/store/apps")]')

    # link to the google play page
    available_in_google_play = WebElement(xpath='//div[@class="apps-color apps-header"]//\
                               a[contains(@href, "play.google.com/store/apps")]')

    # link to the App Store page
    download_to_app_store = WebElement(xpath='//div[@class="apps-color apps-header"]//\
                               a[contains(@href, "itunes.apple.com/us/app")]')

    # link to the App Gallery page
    open_to_app_gallery = WebElement(xpath='//div[@class="apps-color apps-header"]//\
                                   a[contains(@href, "appgallery8.huawei.com")]')
