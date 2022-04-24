from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MyFavoritesPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product/") and contains(@class, "tile-hover-target")]/\
        span/span')
