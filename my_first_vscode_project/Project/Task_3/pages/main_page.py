import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_page(self, url):
        self.open(url)
        self.find_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Клик по «Личный кабинет»')
    def click_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Клик по «Конструктор»')
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Клик по «Лента заказов»')
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('Клик по ингредиенту (булка)')
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT_BUN)

    @allure.step('Закрыть модальное окно крестиком')
    def close_modal(self):
        button = self.find_element(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.driver.execute_script('arguments[0].click();', button)
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step('Клик по «Оформить заказ»')
    def click_place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Получить заголовок конструктора')
    def get_constructor_title(self):
        return self.get_text(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('Получить счётчик ингредиента')
    def get_ingredient_counter(self):
        return int(self.get_text(MainPageLocators.INGREDIENT_BUN_COUNTER))

    @allure.step('Проверить, что модалка ингредиента открыта')
    def is_ingredient_modal_opened(self):
        self.find_element(MainPageLocators.INGREDIENT_MODAL)
        return 'Детали ингредиента' in self.get_text(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step('Проверить, что модалка закрыта')
    def is_modal_closed(self):
        self.wait_for_invisible(MainPageLocators.INGREDIENT_MODAL)
        return True

    @allure.step('Добавить ингредиент в конструктор')
    def add_ingredient_to_constructor(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_BUN,
            MainPageLocators.CONSTRUCTOR_BASKET,
            MainPageLocators.INGREDIENT_BUN_COUNTER,
        )

    @allure.step('Дождаться номера оформленного заказа')
    def wait_for_order_number(self):
        self.find_element(MainPageLocators.ORDER_ID_HINT)
        self.wait_for_invisible(MainPageLocators.ORDER_LOADING_NUMBER)
        return self.get_text(MainPageLocators.ORDER_NUMBER)

    @allure.step('Проверить, что заказ оформлен')
    def is_order_placed(self):
        self.find_element(MainPageLocators.ORDER_ID_HINT)
        return 'идентификатор заказа' in self.get_text(MainPageLocators.ORDER_ID_HINT)
