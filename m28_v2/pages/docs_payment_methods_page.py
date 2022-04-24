from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class DocsPaymentMethods(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    bank_card = WebElement(xpath='//h2[@id="банковская-карта"]')

    ozon_card = WebElement(xpath='//h2[@id="ozon-card"]')

    ozon_account = WebElement(xpath='//h2[@id="ozon-счёт"]')

    ozon_installments = WebElement(xpath='//h2[@id="ozon-рассрочка"]')

    ozon_umoney = WebElement(xpath='//h2[@id="юmoney"]')

    ozon_umoney = WebElement(xpath='//h2[@id="юmoney"]')

    fast_payment_system = WebElement(xpath='//h2[@id="система-быстрых-платежей"]')

    gift_certificate = WebElement(xpath='//h2[@id="подарочный-сертификат"]')

    balance_of_funds = WebElement(xpath='//h2[@id="баланс-средств"]')

    premium_points_and_ozon_points = WebElement(xpath='//h2[@id="premium-баллы-и-баллы-ozon"]')