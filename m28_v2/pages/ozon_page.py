#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os,pickle, time
from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements
from config import url


class OzonPage(WebPage):

    def __init__(self, web_driver):
        super().__init__(web_driver, url)

    def get_shops(self):
        return self._web_driver.find_element_by_xpath("//*[contains(text(), 'Магазины')]")

    def get_brand(self):
        return self._web_driver.find_element_by_xpath("//header//*[contains(text(), 'Бренды')]")

    def press_keybord_enter(self):
        self.select_city_field.keybord_enter()

    def switch_window(self):
        p = self._web_driver.current_window_handle

        # get first child window
        chwd = self._web_driver.window_handles

        for w in chwd:
            # switch focus to child window
            if (w != p):
                self._web_driver.switch_to.window(w)
                break

        print("Child window title: " + self._web_driver.title)

    # Main search field
    search = WebElement(xpath='//input[@placeholder="Искать на Ozon"]')

    # Search button
    search_run_button = WebElement(xpath='//button/*[@aria-label="Поиск"]')

    # City selection button
    city_selection_button = WebElement(xpath='//div[@role="navigation"]//button')

    # Select city field
    select_city_field = WebElement(xpath='//h2/..//input')

    # link to the mobile application page
    mobile_application = WebElement(xpath='//a[contains(@href, "/info/appspromo")]')

    # title of main page
    title_of_main_page = WebElement(xpath='//\
                         title[contains(text(), "OZON — интернет-магазин. Миллионы товаров по выгодным ценам")]')

    # VK link in footer
    footer_vk_link = WebElement(xpath='//a[@title="VK"]')

    # VK link in footer
    footer_telegram_link = WebElement(xpath='//a[@title="Telegram"]')

    # VK link in footer
    footer_ok_link = WebElement(xpath='//a[@title="Одноклассники"]')

    sertificates = WebElement(xpath='//header//a[contains(text(), "Сертификаты")]')

    electronics = WebElement(xpath='//header//a[contains(text(), "Электроника")]')

    clothing_and_shoes = WebElement(xpath='//header//a[contains(text(), "Одежда и обувь")]')

    children_products = WebElement(xpath='//header//a[contains(text(), "Детские товары")]')

    house_and_garden = WebElement(xpath='//header//a[contains(text(), "Дом и сад")]')

    ozon_fresh = WebElement(xpath='//header//a[contains(text(), "Ozon fresh")]')

    ozon_live = WebElement(xpath='//header//a[contains(text(), "LIVE")]')

    ozon_account = WebElement(xpath='//header//a[contains(text(), "Ozon Счёт")]')

    ozon_travel = WebElement(xpath='//header//a[contains(text(), "Ozon Travel")]')

    ozon_premium = WebElement(xpath='//header//a[contains(text(), "Premium")]')

    ozon_top_fashion = WebElement(xpath='//a[contains(@href, "/highlight/top-fashion/")]')

    help = WebElement(xpath='//a[@href="//docs.ozon.ru/common/"]')

    ozon_for_business = WebElement(xpath='//a[@href="/business/?perehod=header"]')

    selL_on_ozon = WebElement(xpath='//div[@role="navigation"]//a[contains(@href, "https://seller.ozon.ru")]')

    earn_with_ozon = WebElement(xpath='//div[@role="navigation"]//\
                     a[contains(@href, "//business.ozon.ru/?perehod=header")]')

    points_issue = WebElement(xpath='//a[@href="/info/map/"]')
