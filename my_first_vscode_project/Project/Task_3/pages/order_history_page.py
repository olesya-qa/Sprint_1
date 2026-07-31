import allure

from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    @allure.step('Дождаться карточки заказа')
    def wait_for_order_card(self):
        self.find_element(OrderHistoryPageLocators.ORDER_CARD)

    @allure.step('Получить название заказа')
    def get_order_title(self):
        return self.get_text(OrderHistoryPageLocators.ORDER_CARD_TITLE)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.get_text(OrderHistoryPageLocators.ORDER_NUMBER)

    @allure.step('Клик по «Лента заказов»')
    def click_order_feed(self):
        self.click(OrderHistoryPageLocators.ORDER_FEED_LINK)
