import allure

from helpers import normalize_order_number
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Открыть ленту заказов')
    def open_page(self, url):
        self.open(url)
        self.find_element(FeedPageLocators.FEED_TITLE)

    @allure.step('Дождаться списка заказов')
    def wait_for_orders_list(self):
        self.find_element(FeedPageLocators.ORDERS_LIST)

    @allure.step('Получить заголовок ленты заказов')
    def get_title(self):
        return self.get_text(FeedPageLocators.FEED_TITLE)

    @allure.step('Клик по первому заказу в ленте')
    def click_first_order(self):
        self.click(FeedPageLocators.FIRST_ORDER_CARD)

    @allure.step('Проверить, что модалка заказа открыта')
    def is_order_modal_opened(self):
        self.find_element(FeedPageLocators.ORDER_MODAL)
        return 'бургер' in self.get_text(FeedPageLocators.ORDER_MODAL_TITLE).lower()

    @allure.step('Получить счётчик «Выполнено за всё время»')
    def get_total_completed(self):
        return int(self.get_text(FeedPageLocators.TOTAL_COMPLETED_COUNTER))

    @allure.step('Получить счётчик «Выполнено за сегодня»')
    def get_today_completed(self):
        return int(self.get_text(FeedPageLocators.TODAY_COMPLETED_COUNTER))

    @allure.step('Дождаться увеличения счётчика «Выполнено за всё время»')
    def wait_total_completed_greater_than(self, previous_value):
        def condition(_):
            try:
                return self.get_total_completed() > previous_value
            except Exception:
                return False

        self.wait_until(condition)
        return self.get_total_completed()

    @allure.step('Дождаться увеличения счётчика «Выполнено за сегодня»')
    def wait_today_completed_greater_than(self, previous_value):
        def condition(_):
            try:
                return self.get_today_completed() > previous_value
            except Exception:
                return False

        self.wait_until(condition)
        return self.get_today_completed()

    @allure.step('Клик по «Конструктор»')
    def click_constructor(self):
        self.click(FeedPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Проверить наличие заказа в ленте')
    def is_order_in_feed(self, order_number):
        expected = normalize_order_number(order_number)

        def condition(driver):
            elements = driver.find_elements(*FeedPageLocators.FEED_ORDER_NUMBERS)
            return any(
                normalize_order_number(element.text) == expected
                for element in elements
                if element.text.strip()
            )

        self.wait_until(condition)
        return True

    @allure.step('Проверить наличие номера заказа в разделе «В работе»')
    def is_order_in_progress(self, order_number):
        expected = normalize_order_number(order_number)

        def condition(driver):
            elements = driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDER_NUMBERS)
            return any(
                normalize_order_number(element.text) == expected
                for element in elements
                if element.text.strip()
            )

        self.wait_until(condition)
        return True
