from pages.base_page import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class CategoryPage(WebPage):

    def __init__(self, web_driver):
        self._web_driver = web_driver

    def sort_products_cheap_first(self):
        self.drop_down_list_sort.click()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_enter()

    def sort_products_expensive_first(self):
        self.drop_down_list_sort.click()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_enter()

    def sort_products_by_discount(self):
        self.drop_down_list_sort.click()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_enter()

    def sort_products_by_new(self):
        self.drop_down_list_sort.click()
        self.drop_down_list_sort.keybord_down()
        self.drop_down_list_sort.keybord_enter()

    def set_filter_russian_n_size(self, size_value):
        return self._web_driver.find_element_by_xpath(f'//div[contains(text(), "Российский размер")]/..//\
        span[contains(@href, "/category/")]//span[text()="{size_value}"]')

    def set_filter_by_author(self, size_value):
        return self._web_driver.find_element_by_xpath(f'//div[contains(text(), "Автор")]/..//\
        span[contains(@href, "/category/")]//span[text()="{size_value}"]')

    def set_filter_by_seller(self, size_value):
        return self._web_driver.find_element_by_xpath(f'//div[contains(text(), "Продавец")]/..//\
        span[contains(@href, "/category/")]//span[text()="{size_value}"]')

    def set_filter_smartphone_line(self, smartphone_line_name):
        return self._web_driver.find_element_by_xpath(f'//div[contains(text(), "Линейка")]/..//\
        span[contains(@href, "/category/")]//span[text()="{smartphone_line_name}"]')

    def set_filter_builtin_memory(self, memory_size):
        return self._web_driver.find_element_by_xpath(f'//div[contains(text(), "Встроенная память")]/..//\
        span[contains(@href, "/category/")]//span[text()="{memory_size}"]')

    def set_filter_brand(self, brand_name):
        return self._web_driver.find_element_by_xpath(f'//div[contains(text(), "Бренды")]/..//\
        a[contains(@href, "/category/")]//span[text()="{brand_name}"]')

    def products_with_size_n(self, size_value):
        return self._web_driver.find_elements_by_xpath(f'//a[contains(@href, "/product/") and contains(@class, "tile-hover-target")]/\
        span/span/../../..//div[text()="{size_value}"]')

    def lower_price_limit_field_delete_n_symbol_and_set(self, delete_number, field_value):
        self.lower_price_limit_field.click()
        for i in range(delete_number):
            self.lower_price_limit_field.keybord_backspace()
            self.lower_price_limit_field.keybord_delete()
        self.lower_price_limit_field = field_value
        self.lower_price_limit_field.keybord_enter()

    def upper_price_limit_field_delete_n_symbol_and_set(self, delete_number, field_value):
        self.upper_price_limit_field.click()
        for i in range(delete_number):
            self.upper_price_limit_field.keybord_backspace()
            self.upper_price_limit_field.keybord_delete()
        self.upper_price_limit_field = field_value
        self.upper_price_limit_field.keybord_enter()

    def lower_reviews_limit_field_delete_n_symbol_and_set(self, delete_number, field_value):
        self.lower_reviews_limit_field.click()
        for i in range(delete_number):
            self.lower_reviews_limit_field.keybord_backspace()
            self.lower_reviews_limit_field.keybord_delete()
        self.lower_reviews_limit_field = field_value
        self.lower_reviews_limit_field.keybord_enter()

    def upper_reviews_limit_field_delete_n_symbol_and_set(self, delete_number, field_value):
        self.upper_reviews_limit_field.click()
        for i in range(delete_number):
            self.upper_reviews_limit_field.keybord_backspace()
            self.upper_reviews_limit_field.keybord_delete()
        self.upper_reviews_limit_field = field_value
        self.upper_reviews_limit_field.keybord_enter()

    def lower_battery_capacity_limit_field_delete_n_symbol_and_set(self, delete_number, field_value):
        self.lower_battery_capacity_limit_field.click()
        for i in range(delete_number):
            self.lower_battery_capacity_limit_field.keybord_backspace()
            self.lower_battery_capacity_limit_field.keybord_delete()
        self.lower_battery_capacity_limit_field = field_value
        self.lower_battery_capacity_limit_field.keybord_enter()

    def upper_battery_capacity_limit_field_delete_n_symbol_and_set(self, delete_number, field_value):
        self.upper_battery_capacity_limit_field.click()
        for i in range(delete_number):
            self.upper_battery_capacity_limit_field.keybord_backspace()
            self.upper_battery_capacity_limit_field.keybord_delete()
        self.upper_battery_capacity_limit_field = field_value
        self.upper_battery_capacity_limit_field.keybord_enter()

    # Titles of the products in search results
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product/") and contains(@class, "tile-hover-target")]/\
                      span/span')

    products_img = ManyWebElements(xpath='//div[contains(@class, "widget-search-result-container")]//\
                   a[contains(@href, "/product/")]//img')

    products_add_favourites = ManyWebElements(xpath='//div[@data-widget="megaPaginator"]//div[@interactive="true"]')

    products_number_reviews = ManyWebElements(xpath='//a[contains(@href, "/product/") and contains(text(), "отзыв")]')

    products_battery_capacity = ManyWebElements(xpath='//span[text()="Емкость аккумулятора, мАч: "]/font[3]')

    # Drop-down list to sort products
    drop_down_list_sort = WebElement(xpath='//div[@role="listbox"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@data-widget="megaPaginator"]//\
                      div/div/span[contains(text(), "₽") and @style="color: var(--ozAccentAlert);"]')

    # Discount of the products in search results
    products_discounts = ManyWebElements(xpath='//\
            div[@style="color: var(--ozWhite1); background-color: var(--ozAccentAlert);"]//span[contains(text(), "%")]')

    products_new = ManyWebElements(xpath='//\
                   span[@style="color: var(--ozAccentSecondary);"]//span[contains(text(), "Новинка")]')

    filter_delivery_time_today = WebElement(xpath='//div[contains(@class, "filter-block")]//span[text()="Сегодня"]')

    filter_delivery_time_today_or_tomorrow = WebElement(xpath='//div[contains(@class, "filter-block")]//\
                                             span[text()="Сегодня или завтра"]')

    filter_delivery_time_up_2_days = WebElement(xpath='//div[contains(@class, "filter-block")]//\
                                     span[text()="До 2 дней"]')

    filter_russian_size = WebElement(xpath='//div[contains(text(), "Российский размер")]/..//\
                          span[contains(@href, "/category/")]//span[text()=37]')

    products_delivery_from_2_hours = ManyWebElements(xpath='//span[contains(@class, "tsBodyM")]//\
                                     font[contains(text(), "За 2 часа")]')

    products_delivery_from_tomorrow = ManyWebElements(xpath='//span[contains(@class, "tsBodyM")]//\
                                      font[contains(text(), "Завтра")]')

    products_delivery_from_after_tomorrow = ManyWebElements(xpath='//span[contains(@class, "tsBodyM")]//\
                                            font[contains(text(), "Послезавтра")]')

    # My favorite page link
    my_favorites = WebElement(xpath='//a[@href="/my/favorites"]')

    # Names of the products seller
    products_seller = ManyWebElements(xpath='//div[@data-widget="megaPaginator"]//b/../../span/font/..')

    # in cart button
    in_cart_button = ManyWebElements(xpath='//div[@data-widget="megaPaginator"]//\
                     button/span/span[contains(text(), "В корзину")]')

    cart_button = WebElement(xpath='//a[@href="/cart"]')

    # Filter by price - lower limit field
    lower_price_limit_field = WebElement(xpath='//div[contains(text(), "Цена")]/..//p[contains(text(), "от")]/..//\
                              input[@type="text"]')

    # Filter by price - upper limit field
    upper_price_limit_field = WebElement(xpath='//div[contains(text(), "Цена")]/..//p[contains(text(), "до")]/..//\
                              input[@type="text"]')

    # Filter by number of reviews - lower limit field
    lower_reviews_limit_field = WebElement(xpath='//div[contains(text(), "Количество отзывов у товара")]/..//\
                                p[contains(text(), "от")]/..//input[@type="text"]')

    # Filter by number of reviews - upper limit field
    upper_reviews_limit_field = WebElement(xpath='//div[contains(text(), "Количество отзывов у товара")]/..//\
                                p[contains(text(), "до")]/..//input[@type="text"]')

    # Filter by battery capacity - lower limit field
    lower_battery_capacity_limit_field = WebElement(xpath='//div[contains(text(), "Емкость аккумулятора")]/..//\
                                         p[contains(text(), "от")]/..//input[@type="text"]')

    # Filter by battery capacity - upper limit field
    upper_battery_capacity_limit_field = WebElement(xpath='//div[contains(text(), "Емкость аккумулятора")]/..//\
                                         p[contains(text(), "до")]/..//input[@type="text"]')

    # link on main page
    main_ozon_link = WebElement(xpath='//header/div[@id="stickyHeader"]/div/a/img[contains(@src, "cdn1.ozone.ru")]')

    home_appliances = WebElement(xpath='//div[@data-widget="catalogHorizontalMenu"]//\
                      a[contains(@href, "/category/bytovaya-tehnika")]')

    workwear_and_safety_shoes = WebElement(xpath='//div[@data-widget="catalogHorizontalMenu"]//\
                                span[contains(text(), "Спецодежда, Спецобувь")]')

    baby_food = WebElement(xpath='//div[@data-widget="catalogHorizontalMenu"]//\
                      a[contains(@href, "/highlight/detskoe-pitanie-i-tovary-dlya-kormleniya")]')

    household_products = WebElement(xpath='//div[@data-widget="objectLine"]//\
                         a[contains(@href, "/category/hozyaystvennye-tovary")]')

    what_is_ozon_fresh = WebElement(xpath='//a[@href="https://www.ozon.ru/special/ozonfresh/"]')
