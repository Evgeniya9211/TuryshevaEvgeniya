#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#

#import time, pickle
import time

import pytest
from pages.petfriends import MainPage
from pages.elements import ManyWebElements
from pages.ozon_page import OzonPage
from pages.shops_page import ShopsPage
from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage
from pages.my_favorites_page import MyFavoritesPage
from pages.brand_page import BrandPage
from pages.appspromo_page import AppsPromoPage
from pages.googleplay_page import GooglePlayPage
from pages.appstore_page import AppStorePage
from pages.appgallery_page import AppGalleryPage
from pages.vk_page import VKPage
from pages.telegram_page import TelegramPage
from pages.ok_page import OKPage
from pages.live_page import LivePage
from pages.finance_ozon_page import FinanceOzonPage
from pages.ozon_travel_page import OzonTravelPage
from pages.highlight_premium_page import HighlightPremiumPage
from pages.top_fashion_page import TopFashionPage
from pages.docs_common_page import DocsCommon
from pages.docs_payment_methods_page import DocsPaymentMethods
from pages.ozon_business_page import OzonBusinessPage
from pages.seller_ozon_page import OzonSellerPage
from pages.business_ozon_page import BusinessOzonPage
from pages.geo_page import GeoPage
import re
from selenium.webdriver.common.action_chains import ActionChains


def test_visit(web_browser):
    """ Test №1: Visit to ozon and check element Shops """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    assert ozon_page.get_shops().is_displayed()


def test_shops_page(web_browser):
    """ Test №2: Vist to ozon/seller and check element Books """

    ozon_page = OzonPage(web_browser)
    ozon_page.get_shops().click()
    ozon_page.wait_page_loaded()

    shops_page = ShopsPage(web_browser)

    assert shops_page.get_books()[1].is_displayed()


def test_check_main_search(web_browser):
    """ Test №3: Make sure main search works fine. """
    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'iPhone 12'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_img.count()

    assert category_page.products_titles.count() > 1

    print(" Products title count = ", category_page.products_titles.count())

    # Make sure user found the relevant products
    for title in category_page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'iphone' in title.lower(), msg


def test_check_wrong_input_in_search(web_browser):
    """ Test №4: Make sure that wrong keyboard layout input works fine. """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    # Try to enter "смартфон" with English keyboard:
    ozon_page.search = 'cvfhnajy'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_img.count()

    assert category_page.products_titles.count() > 1

    print(" Products title count = ", category_page.products_titles.count())

    # Make sure user found the relevant products
    for title in category_page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'смартфон' in title.lower(), msg


def test_check_sort_cheap_first(web_browser):
    """ Test №5: Make sure that sort cheap first works fine.

        Note: this test case will fail because there is a bug in
              sorting products cheap first.
    """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'чайник'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    category_page.drop_down_list_sort.scroll_to_element()
    category_page.sort_products_cheap_first()
    category_page.wait_page_loaded()

    assert category_page.drop_down_list_sort.get_text() == "Сначала дешёвые"

    # Get prices of the products in Search results
    all_prices = category_page.products_prices.get_text()
    category_page.wait_page_loaded()

    # Convert all prices from strings to numbers
    all_prices = [p.replace('\u2009', '') for p in all_prices]
    all_prices = [int(p.replace('₽', '')) for p in all_prices]

    print("       all_prices = ", all_prices)
    print("sorted all_prices = ", sorted(all_prices))

    # while True:
    #     pass

    # Make sure products are sorted cheap first correctly:
    assert all_prices == sorted(all_prices), "Sort cheap first doesn't work!"
    assert all_prices, "The list of all prices is empty!"


def test_check_sort_expensive_first(web_browser):
    """ Test №6: Make sure that sort expensive first works fine """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'утюг'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    category_page.drop_down_list_sort.scroll_to_element()
    category_page.sort_products_expensive_first()
    category_page.wait_page_loaded()

    assert category_page.drop_down_list_sort.get_text() == "Сначала дорогие"

    # Get prices of the products in Search results
    all_prices = category_page.products_prices.get_text()
    category_page.wait_page_loaded()

    # Convert all prices from strings to numbers
    all_prices = [p.replace('\u2009', '') for p in all_prices]
    all_prices = [int(p.replace('₽', '')) for p in all_prices]

    print("       all_prices = ", all_prices)
    print("sorted all_prices = ", sorted(all_prices, reverse=True))

    # Make sure products are sorted expensive_first correctly:
    assert all_prices == sorted(all_prices, reverse=True), "Sort cheap_first doesn't work!"
    assert all_prices, "The list of all prices is empty!"


def test_check_sort_by_discount(web_browser):
    """ Test №7: Make sure that sort by discount works fine

        Note: this test case will fail because there is a bug in
              sorting products by discount.
    """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'телевизор'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    category_page.drop_down_list_sort.scroll_to_element()
    category_page.sort_products_by_discount()
    category_page.wait_page_loaded()

    assert category_page.drop_down_list_sort.get_text() == "По размеру скидки"

    # Get prices of the products in Search results
    all_discounts = category_page.products_discounts.get_text()
    category_page.wait_page_loaded()

    # Convert all prices from strings to numbers
    all_discounts = [p.replace('%', '') for p in all_discounts]
    # String contains a unicode en-dash, not an ASCII hyphen. Replace it:
    all_discounts = [float(re.sub(r'[^\x00-\x7F]+', '-', p)) for p in all_discounts]

    print("       all_prices = ", all_discounts)
    print("sorted all_prices = ", sorted(all_discounts))

    # Make sure products are sorted by discount correctly:
    assert all_discounts == sorted(all_discounts), "Sort by discount doesn't work!"
    assert all_discounts, "The list of all prices is empty!"


def test_check_sort_by_new(web_browser):
    """ Test №8: Make sure that sort by new works fine """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'часы'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    category_page.drop_down_list_sort.scroll_to_element()
    category_page.sort_products_by_new()
    category_page.wait_page_loaded()

    assert category_page.drop_down_list_sort.get_text() == "Новинки"

    # Verify that user can see the list of products:
    assert category_page.products_new.count() == category_page.products_img.count()

    assert category_page.products_titles.count() > 1

    print(" Products title count = ", category_page.products_titles.count())

    # Make sure user found the relevant products
    for title in category_page.products_new.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'новинка' in title.lower(), msg


def test_add_product_in_cart(web_browser):
    """ Test №9: Make sure that can add the product to the cart """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)
    product_page = ProductPage(web_browser)
    cart_page = CartPage(web_browser)

    ozon_page.search = 'холодильник'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    product_on_category_page = category_page.products_titles.get_text()[0]
    category_page.products_titles[0].click()
    category_page.wait_page_loaded()

    product_page.add_in_cart_button_click()
    product_page.wait_page_loaded()
    product_page.go_to_cart_button.click()
    product_page.wait_page_loaded()

    cart_page.refresh()

    # Verify that user add one product:
    product_quantity = int(cart_page.drop_down_list_quantity.get_text()[0])

    assert product_quantity == 1

    print("product_on_category_page = ", product_on_category_page)
    print("    product_on_cart_page = ", cart_page.products_titles.get_text()[0])

    # Make sure user found the relevant products
    assert product_on_category_page == cart_page.products_titles.get_text()[0], "The product in the cart does\
    not match the one added!"


def test_add_ten_identical_products_in_cart(web_browser):
    """ Test №10: Make sure that can add ten identical the product to the cart using the plus symbol """

    product_add_on_plus = 3

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)
    product_page = ProductPage(web_browser)
    cart_page = CartPage(web_browser)

    ozon_page.search = 'тостер'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    product_on_category_page = category_page.products_titles.get_text()[0]
    category_page.products_titles[0].click()

    product_page.add_in_cart_button_click()

    product_page.wait_page_loaded()

    product_page.press_plus_symbol_button_n_times(product_add_on_plus)
    product_page.go_to_cart_button.click()
    product_page.wait_page_loaded()

    cart_page.refresh()

    # Verify that user add 11 products:
    product_quantity = int(cart_page.drop_down_list_quantity.get_text()[0])

    assert product_quantity == (product_add_on_plus + 1)

    print("product_on_category_page = ", product_on_category_page)
    print("    product_on_cart_page = ", cart_page.products_titles.get_text()[0])
    print("    product_quantity     = ", product_quantity)

    # Make sure user found the relevant products
    assert product_on_category_page == cart_page.products_titles.get_text()[0], "The product in the cart does\
        not match the one added!"


def test_delete_ten_identical_products_in_cart(web_browser):
    """ Test №11: Make sure that can delete ten identical the product to the cart using the minus symbol """

    product_add_on_plus = 3

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)
    product_page = ProductPage(web_browser)
    cart_page = CartPage(web_browser)

    ozon_page.search = 'ручки'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    product_on_category_page = category_page.products_titles.get_text()[0]
    category_page.products_titles[0].click()

    product_page.add_in_cart_button_click()

    product_page.wait_page_loaded()
    # Add products on plus
    product_page.press_plus_symbol_button_n_times(product_add_on_plus)

    # while True:
    #     pass

    # Verify that user add (product_add_on_plus+1) products:
    product_quantity = int(product_page.field_quantity_products.get_text()[0])

    assert product_quantity == (product_add_on_plus + 1)

    # Delete products on minus
    product_page.press_minus_symbol_button_n_times(product_add_on_plus)

    # Verify that user add one products after delete:
    product_quantity = int(product_page.field_quantity_products.get_text()[0])

    assert product_quantity == 1


def test_filter_delivery_time_today(web_browser):
    """ Test №12: Make sure that the filter by delivery time is today, it works correctly

        Note: this test case will fail because Number
              all products and number products with delivery time 2 hourse are not equivalent.
    """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'ботинки'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    category_page.filter_delivery_time_today.scroll_to_element()
    category_page.filter_delivery_time_today.click()
    category_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_delivery_from_2_hours.count(), " Number \
           all products and number products with delivery time 2 hourse are not equivalent"


def test_filters_delivery_time_today_or_tomorrow(web_browser):
    """ Test №13: Make sure that the filter by delivery time is today or tomorrow, it works correctly """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'ботинки'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    category_page.filter_delivery_time_today_or_tomorrow.scroll_to_element()
    category_page.filter_delivery_time_today_or_tomorrow.click()
    category_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_delivery_from_tomorrow.count()
    assert category_page.products_titles, "The list of products is empty!"


def test_filter_delivery_time_up_2_days(web_browser):
    """ Test №14: Make sure that the filter by delivery time is up to 2 days, it works correctly """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'ботинки'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    category_page.filter_delivery_time_up_2_days.scroll_to_element()
    category_page.filter_delivery_time_up_2_days.click()
    category_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == (category_page.products_delivery_from_tomorrow.count() +
                                                     category_page.products_delivery_from_after_tomorrow.count())
    assert category_page.products_titles, "The list of products is empty!"


def test_filter_russian_size(web_browser):
    """ Test №15: Make sure that the filter by parametrize russian size, it works correctly """

    size = 40

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'ботинки'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    size_n_set = category_page.set_filter_russian_n_size(size)
    size_n_set.click()
    category_page.wait_page_loaded()

    list_products_with_size_n = category_page.products_with_size_n(size)

    print(f'Number product with size = {size}:', len(list_products_with_size_n))

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == len(list_products_with_size_n)
    assert category_page.products_titles, "The list of products is empty!"


def test_product_add_to_favorites(web_browser):
    """ Test №16: Make sure that the product is correctly added to favorites """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)
    my_favorite_page = MyFavoritesPage(web_browser)

    ozon_page.search = 'кросовки'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    title_test_product = category_page.products_titles.get_text()[0]
    category_page.products_add_favourites.scroll_to_element()
    category_page.products_add_favourites[0].click()
    category_page.wait_page_loaded()

    category_page.my_favorites.scroll_to_element()
    category_page.my_favorites.click()
    category_page.wait_page_loaded()

    print("Name product from Category page:    ", title_test_product)
    print("Name product from My Favorite page: ", my_favorite_page.products_titles.get_text()[0])

    assert my_favorite_page.products_titles.get_text()[0] == title_test_product, "the name of the test product from the\
    Category page and the My Favorites page are not identical"
    assert my_favorite_page.products_titles, "The list of products on my favorite page is empty!"


def test_filter_by_author(web_browser):
    """ Test №17: Make sure that the filter by author, it works correctly

        Note: this test case will fail because there is a bug in
              filter by author.
    """

    author_name = "Киркман Роберт"

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'комиксы'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    author_filter_set = category_page.set_filter_by_author(author_name)
    author_filter_set.click()
    category_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_img.count()

    print(f'Number filtered products = ', category_page.products_titles.count())

    assert category_page.products_titles, "The list of products on my favorite page is empty!"

    # Make sure user found the relevant products
    for title in category_page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{author_name.lower()}' in title.lower(), msg


def test_filter_by_seller(web_browser):
    """ Test №18: Make sure that the filter by seller, it works correctly """

    seller_name = "MARVEL"

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'смартфоны'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    seller_filter_set = category_page.set_filter_by_seller(seller_name)
    seller_filter_set.click()
    category_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_seller.count()

    assert category_page.products_seller, "The list of products on my favorite page is empty!"

    # Make sure user found the relevant products
    for title in category_page.products_seller.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{seller_name.lower()}' in title.lower(), msg


def test_all_products_deleting_from_cart(web_browser):
    """ Test №19: Make sure that removing all products from the basket, it works correctly """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)
    cart_page = CartPage(web_browser)

    ozon_page.search = 'сандали'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    # Add to cart two products
    category_page.in_cart_button[0].click()
    category_page.in_cart_button[1].click()
    category_page.cart_button.click()
    category_page.wait_page_loaded()

    cart_page.refresh()

    assert cart_page.products_titles.count() == 2, "There are not two items in the cart"

    cart_page.delete_selected_button.click()
    cart_page.wait_page_loaded()

    cart_page.confirmation_delete_selected_button.click()
    cart_page.wait_page_loaded()

    assert cart_page.cart_empty_message.is_presented(), "Don't see message - your shopping cart is empty"


def test_filter_by_price(web_browser):
    """ Test №20: Make sure that filter bt price, it works correctly """

    lower_price_limit = 30000
    upper_price_limit = 50000

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'смартфоны'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    category_page.upper_price_limit_field.scroll_to_element()
    category_page.upper_price_limit_field_delete_n_symbol_and_set(20, upper_price_limit)
    category_page.wait_page_loaded()

    category_page.lower_price_limit_field.scroll_to_element()
    category_page.lower_price_limit_field_delete_n_symbol_and_set(20, lower_price_limit)
    category_page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = category_page.products_prices.get_text()
    category_page.wait_page_loaded()

    # Convert all prices from strings to numbers
    all_prices = [p.replace('\u2009', '') for p in all_prices]
    all_prices = [int(p.replace('₽', '')) for p in all_prices]

    print("       all_prices = ", all_prices)

    for product_price in all_prices:
        assert lower_price_limit <= product_price <= upper_price_limit, "Found product price in not price limit!"


def test_filter_by_number_of_reviews(web_browser):
    """ Test №21: Make sure that filter by number of reviews, it works correctly """

    lower_reviews_limit = 100
    upper_reviews_limit = 200

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'смартфоны'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    category_page.upper_reviews_limit_field.scroll_to_element()
    category_page.upper_reviews_limit_field_delete_n_symbol_and_set(20, upper_reviews_limit)
    category_page.wait_page_loaded()

    category_page.lower_reviews_limit_field.scroll_to_element()
    category_page.lower_reviews_limit_field_delete_n_symbol_and_set(20, lower_reviews_limit)
    category_page.wait_page_loaded()

    # Get number of reviews of the products in Search results
    all_number_reviews = category_page.products_number_reviews.get_text()
    category_page.wait_page_loaded()

    # Convert all prices from strings to numbers
    all_number_reviews = [p.replace(' отзывов', '') for p in all_number_reviews]
    all_number_reviews = [p.replace(' отзыва', '') for p in all_number_reviews]
    all_number_reviews = [int(p.replace(' отзыв', '')) for p in all_number_reviews]

    print("DEBUG: all_number_reviews = ", all_number_reviews)

    for product_reviews in all_number_reviews:
        assert lower_reviews_limit <= product_reviews <= upper_reviews_limit, "Found product number of reviews in \
        not reviews limit!"


def test_filter_by_smartphone_line(web_browser):
    """ Test №22: Make sure that filter by smartphone line, it works correctly

        Note: this test case will fail because smartphone_line not presented in product title.
    """

    smartphone_line = "Apple iPhone 13"

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'смартфоны'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    smartphone_line_filter_locator = category_page.set_filter_smartphone_line(smartphone_line)
    smartphone_line_filter_locator.click()
    category_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_img.count()

    assert category_page.products_titles, "The list of products is empty!"

    # Make sure user found the relevant products
    for title in category_page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{smartphone_line.lower()}' in title.lower(), msg


def test_filter_by_builtin_memory(web_browser):
    """ Test №23: Make sure that filter by built-in ,memory, it works correctly

        Note: this test case will fail because memory_size not presented in product title.
    """

    memory_size = "64-128 ГБ"

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'смартфоны'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    builtin_memory_filter_locator = category_page.set_filter_builtin_memory(memory_size)
    builtin_memory_filter_locator.click()
    category_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_img.count()

    assert category_page.products_titles, "The list of products is empty!"

    memory_size_replace_gb = memory_size.replace(' ГБ', 'GB')

    print("memory_size_replace_gb = ", memory_size_replace_gb)
    print("products_titles        = ", category_page.products_titles.get_text())

    # Make sure user found the relevant products
    for title in category_page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{memory_size_replace_gb.lower()}' in title.lower(), msg


def test_filter_by_battery_capacity(web_browser):
    """ Test №24: Make sure that filter by battery capacity, it works correctly """

    lower_battery_capacity_limit = 4000
    upper_battery_capacity_limit = 6000

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'смартфоны'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    category_page.upper_battery_capacity_limit_field.scroll_to_element()
    category_page.upper_battery_capacity_limit_field_delete_n_symbol_and_set(20, upper_battery_capacity_limit)
    category_page.wait_page_loaded()

    category_page.lower_battery_capacity_limit_field.scroll_to_element()
    category_page.lower_battery_capacity_limit_field_delete_n_symbol_and_set(20, lower_battery_capacity_limit)
    category_page.wait_page_loaded()

    all_battery_capacity = category_page.products_battery_capacity.get_text()
    category_page.wait_page_loaded()

    print("DEBUG: all_battery_capacity = ", all_battery_capacity)

    for product_battery_capacity in all_battery_capacity:
        assert lower_battery_capacity_limit <= int(product_battery_capacity) <= upper_battery_capacity_limit, \
            "Found product battery capacity in not capacity limit!"


def test_filter_by_brand(web_browser):
    """ Test №25: Make sure that filter by brand, it works correctly """

    brand_name = "Xiaomi"

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)

    ozon_page.search = 'смартфоны'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    brand_filter_locator = category_page.set_filter_brand(brand_name)
    brand_filter_locator.click()
    category_page.wait_page_loaded()

    # Verify that user can see the list of products:
    assert category_page.products_titles.count() == category_page.products_img.count()

    assert category_page.products_titles, "The list of products is empty!"

    # Make sure user found the relevant products
    for title in category_page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{brand_name.lower()}' in title.lower(), msg


def test_city_selection(web_browser):
    """ Test №26: Make sure that city selection, it works correctly """

    city_name = 'Ливны'

    ozon_page = OzonPage(web_browser)

    start_city = ozon_page.city_selection_button.get_text()
    ozon_page.city_selection_button.click()
    ozon_page.wait_page_loaded()

    ozon_page.select_city_field = city_name
    ozon_page.wait_page_loaded()
    ozon_page.press_keybord_enter()
    ozon_page.wait_page_loaded()

    assert start_city != ozon_page.city_selection_button.get_text(), "The name of start city is same as the \
                                                                     selected name"


def test_download_to_google_play_page(web_browser):
    """ Test №27: Visit to ozon/info/appspromo/ and check go to the page Google Play

        Note: this test case will fail because Google Play not work in Russia.
    """

    ozon_page = OzonPage(web_browser)
    appspromo_page = AppsPromoPage(web_browser)
    googleplay_page = GooglePlayPage(web_browser)

    ozon_page.wait_page_loaded()

    ozon_page.mobile_application.click()
    ozon_page.wait_page_loaded()

    assert appspromo_page.available_in_google_play.is_presented(), "Link to the google play page not presented"

    appspromo_page.get_available_in_google_play().click()
    appspromo_page.wait_page_loaded()

    ozon_page.switch_window()
    googleplay_page.wait_page_loaded()

    assert googleplay_page.ozon_app_title.is_presented(), "ozon application title on Google Play not presented"


def test_download_to_appstore_page(web_browser):
    """ Test №28: Visit to ozon/info/appspromo/ and check go to the page App Store """

    ozon_page = OzonPage(web_browser)
    appspromo_page = AppsPromoPage(web_browser)
    appstore_page = AppStorePage(web_browser)

    ozon_page.wait_page_loaded()

    ozon_page.mobile_application.click()
    ozon_page.wait_page_loaded()

    assert appspromo_page.download_to_app_store.is_presented(), "Link to the App Store page not presented"

    appspromo_page.get_download_appstore().click()
    appstore_page.wait_page_loaded()

    ozon_page.switch_window()
    appstore_page.wait_page_loaded()

    ozon_site_link_is_visible = appstore_page.ozon_site_link.is_visible()

    assert ozon_site_link_is_visible, "ozon application title on App Store not visible"


def test_download_to_appgallery_page(web_browser):
    """ Test №29: Visit to ozon/info/appspromo/ and check go to the page App Gallery """

    ozon_page = OzonPage(web_browser)
    appspromo_page = AppsPromoPage(web_browser)
    appgallery_page = AppGalleryPage(web_browser)

    ozon_page.wait_page_loaded()

    ozon_page.mobile_application.click()
    ozon_page.wait_page_loaded()

    assert appspromo_page.open_to_app_gallery.is_presented(), "Link to the App Gallery page not presented"

    appspromo_page.open_to_app_gallery.click()
    appspromo_page.wait_page_loaded()

    ozon_page.switch_window()
    appgallery_page.wait_page_loaded()

    ozon_site_link_is_visible = appgallery_page.ozon_site_link.is_visible()

    assert ozon_site_link_is_visible, "ozon application title on App Gallery not visible"


def test_switch_from_other_ozone_pages_to_main_page(web_browser):
    """ Test №30: Test switching from other ozone pages by clicking the Ozon button to the main page """

    ozon_page = OzonPage(web_browser)
    category_page = CategoryPage(web_browser)
    ozon_page.wait_page_loaded()

    ozon_page.search = 'iPhone 12'
    ozon_page.search_run_button.click()
    ozon_page.wait_page_loaded()

    assert category_page.products_delivery_from_2_hours.is_presented(), "check element on category page is false"

    category_page.main_ozon_link.click()
    category_page.wait_page_loaded()

    assert ozon_page.title_of_main_page.is_presented(), "Title of main page not presented"


def test_points_of_issue_page(web_browser):
    """ Test №31: Visit to ozon/geo and check element 'пункты выдачи заказов OZON' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.points_issue.click()
    ozon_page.wait_page_loaded()

    geo_page = GeoPage(web_browser)

    assert geo_page.ozon_order_pickup_points.is_visible(), "'Развивайте бизнес и зарабатывайте вместе \
                                                                           с нами' not visible"


def test_footer_vk_link(web_browser):
    """ Test №32: Check the VK link in the footer """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    vk_page = VKPage(web_browser)

    ozon_page.footer_vk_link.scroll_to_element()
    ozon_page.footer_vk_link.click()
    ozon_page.wait_page_loaded()

    ozon_page.switch_window()
    vk_page.wait_page_loaded()

    vk_page.screenshot()

    assert vk_page.title_of_vk_page.is_presented(), "Title on VK page not found"


def test_footer_telegram_link(web_browser):
    """ Test №33: Check the Telegram link in the footer """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    telegram_page = TelegramPage(web_browser)

    ozon_page.footer_telegram_link.scroll_to_element()
    ozon_page.footer_telegram_link.click()
    ozon_page.wait_page_loaded()

    ozon_page.switch_window()
    telegram_page.wait_page_loaded()

    telegram_page.screenshot()

    assert telegram_page.title_of_telegram_page.is_presented(), "Title on Telegram page not found"


def test_footer_ok_link(web_browser):
    """ Test №34: Check the OK link in the footer """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ok_page = OKPage(web_browser)

    ozon_page.footer_ok_link.scroll_to_element()
    ozon_page.footer_ok_link.click()
    ozon_page.wait_page_loaded()

    ozon_page.switch_window()
    ok_page.wait_page_loaded()

    ok_page.screenshot()

    assert ok_page.title_of_ok_page.is_presented(), "Title on OK page not found"


def test_brand_page(web_browser):
    """ Test №35: Visit to ozon/brand and check element Apple """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.get_brand().click()
    ozon_page.wait_page_loaded()

    brand_page = BrandPage(web_browser)

    assert brand_page.get_apple().is_displayed()


def test_certificates_page(web_browser):
    """ Test №36: Visit to ozon/product/elektronnyy-podarochnyy-sertifikat-million-podarkov and
        check element Certificates

        Note: this test case will fail because there sertificates is present in Firefox browser.
            Chrome browser not have this page."""

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()

    assert ozon_page.sertificates.is_visible(), "Sertificates is not present on main page"

    ozon_page.sertificates.click()
    ozon_page.wait_page_loaded()

    product_page = ProductPage(web_browser)

    assert product_page.get_elektronnyy_podarochnyy_sertifikat_million_podarkov().is_visible(), " \
                                                  elektronnyy-podarochnyy-sertifikat-million-podarkov is not presented"


def test_electronics_page(web_browser):
    """ Test №37: Visit to ozon/category/elektronika and check element 'Бытовая техника' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.electronics.click()
    ozon_page.wait_page_loaded()

    category_page = CategoryPage(web_browser)

    assert category_page.home_appliances.is_visible(), "home appliances is not visible"


def test_clothing_and_shoes_page(web_browser):
    """ Test №38: Visit to ozon/category/zhenskaya-odezhda and check element 'Спецодежда, спецобувь' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.clothing_and_shoes.click()
    ozon_page.wait_page_loaded()

    category_page = CategoryPage(web_browser)

    assert category_page.workwear_and_safety_shoes.is_visible(), "workwear and safety shoes is not visible"


def test_children_products_page(web_browser):
    """ Test №39: Visit to ozon/category/detskie-tovary and check element 'Детское питание' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.children_products.click()
    ozon_page.wait_page_loaded()

    category_page = CategoryPage(web_browser)

    assert category_page.baby_food.is_visible(), "baby food is not visible"


def test_house_and_garden_page(web_browser):
    """ Test №40: Visit to ozon/category/dom-i-sad and check element 'Хозяйственные товары' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.house_and_garden.click()
    ozon_page.wait_page_loaded()

    category_page = CategoryPage(web_browser)

    assert category_page.household_products.is_visible(), "baby food is not visible"


def test_ozon_fresh_page(web_browser):
    """ Test №41: Visit to ozon/category/supermarket and check element 'что такоe Ozone fresh' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.ozon_fresh.click()
    ozon_page.wait_page_loaded()

    category_page = CategoryPage(web_browser)

    assert category_page.what_is_ozon_fresh.is_visible(), "what is ozon fresh banner not visible"


def test_ozon_live_page(web_browser):
    """ Test №42: Visit to ozon/live and check element 'OZON Live' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.ozon_live.click()
    ozon_page.wait_page_loaded()

    live_page = LivePage(web_browser)

    assert live_page.header_ozon_live.is_visible(), "OZON Live not visible"


def test_ozon_account_page(web_browser):
    """ Test №43: Visit to finance-ozon-ru and check element 'Open Ozon account' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.ozon_account.click()
    ozon_page.wait_page_loaded()

    finance_ozon_page = FinanceOzonPage(web_browser)
    finance_ozon_page.open_ozon_account.scroll_to_element()

    assert finance_ozon_page.open_ozon_account.is_visible(), "OZON Live not visible"


def test_ozon_travel_page(web_browser):
    """ Test №44: Visit to ozon/travel and check element 'Search for cheap flights' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.ozon_travel.click()
    ozon_page.wait_page_loaded()

    ozon_travel_page = OzonTravelPage(web_browser)

    assert ozon_travel_page.serch_for_cheap_flights.is_visible(), "Search for cheap flights not visible"


def test_ozon_premium_page(web_browser):
    """ Test №45: Visit to ozon/highlight/premium and check element 'Подписка на кешбэк, бесплатную доставку, кино,
        курсы и ранний доступ к распродажам' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.ozon_premium.click()
    ozon_page.wait_page_loaded()

    highlight_premium_page = HighlightPremiumPage(web_browser)

    assert highlight_premium_page.cashback_subscription.is_visible(), "'Подписка на кешбэк, бесплатную доставку, кино,\
        курсы и ранний доступ к распродажам' not visible"


def test_top_fashion_page(web_browser):
    """ Test №46: Visit to ozon/highlight/top-fashion and check element 'TOP fashion' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.ozon_top_fashion.click()
    ozon_page.wait_page_loaded()

    top_fashion_page = TopFashionPage(web_browser)

    assert top_fashion_page.top_fashion.is_visible(), "TOP fashion not visible"


def test_check_payment_methods_page(web_browser):
    """ Test №47: Visit to docs-ozon-ru/common/oplata/sposoby-oplaty/ and check all elements payment methods """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.help.click()
    ozon_page.wait_page_loaded()

    docs_common_page = DocsCommon(web_browser)
    docs_common_page.payment_methods.click()
    docs_common_page.wait_page_loaded()

    docs_payment_methods = DocsPaymentMethods(web_browser)

    docs_payment_methods.premium_points_and_ozon_points.scroll_to_element()
    assert docs_payment_methods.premium_points_and_ozon_points.is_visible(), "premium points and ozon points not visible"

    docs_payment_methods.ozon_account.scroll_to_element()
    assert docs_payment_methods.ozon_account.is_visible(), "ozon account not visible"

    docs_payment_methods.balance_of_funds.scroll_to_element()
    assert docs_payment_methods.balance_of_funds.is_visible(), "balance of funds not visible"

    docs_payment_methods.bank_card.scroll_to_element()
    assert docs_payment_methods.bank_card.is_visible(), "bank card not visible"

    docs_payment_methods.fast_payment_system.scroll_to_element()
    assert docs_payment_methods.fast_payment_system.is_visible(), "fast payment system not visible"

    docs_payment_methods.gift_certificate.scroll_to_element()
    assert docs_payment_methods.gift_certificate.is_visible(), "gift certificate not visible"

    docs_payment_methods.ozon_card.scroll_to_element()
    assert docs_payment_methods.ozon_card.is_visible(), "ozon card not visible"

    docs_payment_methods.ozon_installments.scroll_to_element()
    assert docs_payment_methods.ozon_installments.is_visible(), "ozon installments not visible"

    docs_payment_methods.ozon_umoney.scroll_to_element()
    assert docs_payment_methods.ozon_umoney.is_visible(), "ozon umoney not visible"


def test_ozon_for_business_page(web_browser):
    """ Test №48: Visit to ozon/business and check element 'Всё для вашего
        бизнеса на Ozon' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.ozon_for_business.click()
    ozon_page.wait_page_loaded()

    ozon_business_page = OzonBusinessPage(web_browser)

    assert ozon_business_page.everything_for_your_business_on_ozon.is_visible(), "'Всё для вашего \
        бизнеса на Ozon' not visible"


def test_ozon_seller_page(web_browser):
    """ Test №49: Visit to seller-ozon-business and check element 'Любому бизнесу найдётся место на Ozon' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.selL_on_ozon.click()
    ozon_page.wait_page_loaded()

    ozon_seller_page = OzonSellerPage(web_browser)

    assert ozon_seller_page.place_for_any_business_on_ozon.is_visible(), "'Любому бизнесу найдётся место на Ozon' \
           not visible"


def test_business_page(web_browser):
    """ Test №50: Visit to test_business_page-ozon-ru and check element 'Развивайте бизнес
        и зарабатывайте вместе с нами' """

    ozon_page = OzonPage(web_browser)
    ozon_page.wait_page_loaded()
    ozon_page.earn_with_ozon.click()
    ozon_page.wait_page_loaded()

    business_ozon_page = BusinessOzonPage(web_browser)

    assert business_ozon_page.develop_your_business.is_visible(), "'Развивайте бизнес и зарабатывайте вместе \
                                                                           с нами' not visible"


