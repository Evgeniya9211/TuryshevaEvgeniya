Tests:

test_visit                                      - Test №1:  Visit to ozon and check element Shops
test_shops_page                                 - Test №2:  Vist to ozon.ru/seller and check element Books
test_check_main_search                          - Test №3:  Make sure main search works fine
test_check_wrong_input_in_search                - Test №4:  Make sure that wrong keyboard layout input works fine
test_check_sort_cheap_first                     - Test №5:  Make sure that sort cheap first works fine
test_check_sort_expensive_first                 - Test №6:  Make sure that sort expensive first works fine
test_check_sort_by_discount                     - Test №7:  Make sure that sort by discount works fine
test_check_sort_by_new                          - Test №8:  Make sure that sort by new works fine
test_add_product_in_cart                        - Test №9:  Make sure that can add the product to the cart
test_add_ten_identical_products_in_cart         - Test №10: Make sure that can add ten identical the product to the cart using the plus symbol
test_delete_ten_identical_products_in_cart      - Test №11: Make sure that can delete ten identical the product to the cart using the minus symbol
test_filter_delivery_time_today                 - Test №12: Make sure that the filter by delivery time is today, it works correctly
test_filters_delivery_time_today_or_tomorrow    - Test №13: Make sure that the filter by delivery time is today or tomorrow, it works correctly
test_filter_delivery_time_up_2_days             - Test №14: Make sure that the filter by delivery time is up to 2 days, it works correctly
test_filter_russian_size                        - Test №15: Make sure that the filter by parametrize russian size, it works correctly
test_product_add_to_favorites                   - Test №16: Make sure that the product is correctly added to favorites
test_filter_by_author                           - Test №17: Make sure that the filter by author, it works correctly Note: this test case will fail because there is a bug in filter by author
test_filter_by_seller                           - Test №18: Make sure that the filter by seller, it works correctly
test_all_products_deleting_from_cart            - Test №19: Make sure that removing all products from the basket, it works correctly
test_filter_by_price                            - Test №20: Make sure that filter bt price, it works correctly
test_filter_by_number_of_reviews                - Test №21: Make sure that filter by number of reviews, it works correctly
test_filter_by_smartphone_line                  - Test №22: Make sure that filter by smartphone line, it works correctly
test_filter_by_builtin_memory                   - Test №23: Make sure that filter by built-in ,memory, it works correctly
test_filter_by_battery_capacity                 - Test №24: Make sure that filter by battery capacity, it works correctly
test_filter_by_brand                            - Test №25: Make sure that filter by brand, it works correctly
test_city_selection                             - Test №26: Make sure that city selection, it works correctly
test_download_to_google_play_page               - Test №27: Visit to ozon/info/appspromo/ and check go to the page Google Play
test_download_to_appstore_page                  - Test №28: Visit to ozon/info/appspromo/ and check go to the page App Store
test_download_to_appgallery_page                - Test №29: Visit to ozon/info/appspromo/ and check go to the page App Gallery
test_switch_from_other_ozone_pages_to_main_page - Test №30: Test switching from other ozone pages by clicking the Ozon button to the main page
test_points_of_issue_page                       - Test №31: Visit to ozon/geo and check element 'пункты выдачи заказов OZON'
test_footer_vk_link                             - Test №32: Check the VK link in the footer
test_footer_telegram_link                       - Test №33: Check the Telegram link in the footer
test_footer_ok_link                             - Test №34: Check the OK link in the footer
test_brand_page                                 - Test №35: Visit to ozon/brand and check element Apple
test_certificates_page                          - Test №36: Visit to ozon/product/elektronnyy-podarochnyy-sertifikat-million-podarkov and check element Certificates
test_electronics_page                           - Test №37: Visit to ozon/category/elektronika and check element 'Бытовая техника'
test_clothing_and_shoes_page                    - Test №38: Visit to ozon/category/zhenskaya-odezhda and check element 'Спецодежда, спецобувь'
test_children_products_page                     - Test №39: Visit to ozon/category/detskie-tovary and check element 'Детское питание'
test_house_and_garden_page                      - Test №40: Visit to ozon/category/dom-i-sad and check element 'Хозяйственные товары'
test_ozon_fresh_page                            - Test №41: Visit to ozon/category/supermarket and check element 'что такоe Ozone fresh'
test_ozon_live_page                             - Test №42: Visit to ozon/live and check element 'OZON Live'
test_ozon_account_page                          - Test №43: Visit to finance-ozon-ru and check element 'Open Ozon account'
test_ozon_travel_page                           - Test №44: Visit to ozon/travel and check element 'Search for cheap flights'
test_ozon_premium_page                          - Test №45: Visit to ozon/highlight/premium and check element 'Подписка на кешбэк, бесплатную доставку, кино, курсы и ранний доступ к распродажам'
test_top_fashion_page                           - Test №46: Visit to ozon/highlight/top-fashion and check element 'TOP fashion'
test_check_payment_methods_page                 - Test №47: Visit to docs-ozon-ru/common/oplata/sposoby-oplaty/ and check all elements payment methods
test_ozon_for_business_page                     - Test №48: Visit to ozon/business and check element 'Всё для вашего бизнеса на Ozon'
test_ozon_seller_page                           - Test №49: Visit to seller-ozon-business and check element 'Любому бизнесу найдётся место на Ozon'
test_business_page                              - Test №50: Visit to test_business_page-ozon-ru and check element 'Развивайте бизнес и зарабатывайте вместе с нами'

How run:

single test: 
	py -m pytest -v -s --driver Chrome --driver-path ./tests/chromedriver.exe -k "test_name"
	
all tests:
	py -m pytest -v -s --driver Chrome --driver-path ./tests/chromedriver.exe .\tests\test_selenium_ozone_pytest.py
	