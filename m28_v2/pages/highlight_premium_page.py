from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class HighlightPremiumPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    cashback_subscription = WebElement(xpath='//\
    h1[contains(text(), "Подписка на кешбэк, бесплатную доставку, кино, курсы и ранний доступ к распродажам")]')
