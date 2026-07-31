import allure

from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage
from urls import FEED_URL, MAIN_URL


@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Клик по заказу открывает детали')
    def test_order_modal_opens(self, driver):
        feed_page = FeedPage(driver)

        feed_page.open_page(FEED_URL)
        feed_page.click_first_order()

        assert feed_page.is_order_modal_opened()

    @allure.title('Заказы из истории отображаются в ленте заказов')
    def test_user_orders_shown_in_feed(self, authorized_driver, user_with_order):
        main_page = MainPage(authorized_driver)
        profile_page = ProfilePage(authorized_driver)
        order_history_page = OrderHistoryPage(authorized_driver)
        feed_page = FeedPage(authorized_driver)

        main_page.open_page(MAIN_URL)
        main_page.click_personal_account()
        profile_page.wait_for_profile()
        profile_page.click_order_history()
        order_history_page.wait_for_order_card()
        order_number = order_history_page.get_order_number()
        order_history_page.click_order_feed()
        feed_page.wait_for_orders_list()

        assert feed_page.is_order_in_feed(order_number)

    @allure.title('Счётчик «Выполнено за всё время» увеличивается')
    def test_total_completed_counter_increases(self, authorized_driver):
        feed_page = FeedPage(authorized_driver)
        main_page = MainPage(authorized_driver)

        feed_page.open_page(FEED_URL)
        total_before = feed_page.get_total_completed()
        feed_page.click_constructor()
        main_page.find_element(MainPageLocators.CONSTRUCTOR_BASKET)
        main_page.add_ingredient_to_constructor()
        main_page.click_place_order()
        main_page.wait_for_order_number()
        main_page.close_modal()
        feed_page.open_page(FEED_URL)
        total_after = feed_page.wait_total_completed_greater_than(total_before)

        assert total_after > total_before

    @allure.title('Счётчик «Выполнено за сегодня» увеличивается')
    def test_today_completed_counter_increases(self, authorized_driver):
        feed_page = FeedPage(authorized_driver)
        main_page = MainPage(authorized_driver)

        feed_page.open_page(FEED_URL)
        today_before = feed_page.get_today_completed()
        feed_page.click_constructor()
        main_page.find_element(MainPageLocators.CONSTRUCTOR_BASKET)
        main_page.add_ingredient_to_constructor()
        main_page.click_place_order()
        main_page.wait_for_order_number()
        main_page.close_modal()
        feed_page.open_page(FEED_URL)
        today_after = feed_page.wait_today_completed_greater_than(today_before)

        assert today_after > today_before

    @allure.title('Номер заказа появляется в разделе «В работе»')
    def test_order_number_appears_in_progress(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        feed_page = FeedPage(authorized_driver)

        main_page.open_page(MAIN_URL)
        main_page.add_ingredient_to_constructor()
        main_page.click_place_order()
        order_number = main_page.wait_for_order_number()
        main_page.close_modal()
        main_page.click_order_feed()

        assert feed_page.is_order_in_progress(order_number)
