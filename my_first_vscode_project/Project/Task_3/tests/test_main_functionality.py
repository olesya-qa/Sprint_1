import allure

from locators.main_page_locators import MainPageLocators
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from urls import FEED_URL, MAIN_URL


@allure.feature('Основной функционал')
class TestMainFunctionality:

    @allure.title('Переход по клику на «Конструктор»')
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        feed_page.open_page(FEED_URL)
        main_page.click_constructor()
        main_page.find_element(MainPageLocators.CONSTRUCTOR_TITLE)

        assert main_page.get_current_url() == MAIN_URL
        assert 'Соберите бургер' in main_page.get_constructor_title()

    @allure.title('Переход по клику на «Лента заказов»')
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        main_page.open_page(MAIN_URL)
        main_page.click_order_feed()
        feed_page.wait_for_orders_list()

        assert main_page.get_current_url() == FEED_URL
        assert 'Лента заказов' in feed_page.get_title()

    @allure.title('Клик по ингредиенту открывает детали')
    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(MAIN_URL)
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_opened()

    @allure.title('Модалка ингредиента закрывается крестиком')
    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)

        main_page.open_page(MAIN_URL)
        main_page.click_ingredient()
        main_page.is_ingredient_modal_opened()
        main_page.close_modal()

        assert main_page.is_modal_closed()

    @allure.title('Счётчик ингредиента увеличивается при добавлении')
    def test_ingredient_counter_increases(self, authorized_driver):
        main_page = MainPage(authorized_driver)

        main_page.open_page(MAIN_URL)
        counter_before = main_page.get_ingredient_counter()
        main_page.add_ingredient_to_constructor()
        counter_after = main_page.get_ingredient_counter()

        assert counter_after > counter_before

    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_authorized_user_can_place_order(self, authorized_driver):
        main_page = MainPage(authorized_driver)

        main_page.open_page(MAIN_URL)
        main_page.add_ingredient_to_constructor()
        main_page.click_place_order()

        assert main_page.is_order_placed()
