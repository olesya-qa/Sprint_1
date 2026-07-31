import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage
from urls import LOGIN_URL, MAIN_URL, ORDER_HISTORY_URL, PROFILE_URL


@allure.feature('Личный кабинет')
class TestPersonalAccount:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_navigate_to_personal_account(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        profile_page = ProfilePage(authorized_driver)

        main_page.open_page(MAIN_URL)
        main_page.click_personal_account()
        profile_page.wait_for_profile()

        assert profile_page.get_current_url() == PROFILE_URL
        assert 'персональные данные' in profile_page.get_profile_hint()

    @allure.title('Переход в раздел «История заказов»')
    def test_navigate_to_order_history(self, authorized_driver, user_with_order):
        main_page = MainPage(authorized_driver)
        profile_page = ProfilePage(authorized_driver)
        order_history_page = OrderHistoryPage(authorized_driver)

        main_page.open_page(MAIN_URL)
        main_page.click_personal_account()
        profile_page.wait_for_profile()
        profile_page.click_order_history()
        order_history_page.wait_for_order_card()

        assert order_history_page.get_current_url() == ORDER_HISTORY_URL
        assert 'бургер' in order_history_page.get_order_title().lower()

    @allure.title('Выход из аккаунта')
    def test_logout(self, authorized_driver):
        main_page = MainPage(authorized_driver)
        profile_page = ProfilePage(authorized_driver)
        login_page = LoginPage(authorized_driver)

        main_page.open_page(MAIN_URL)
        main_page.click_personal_account()
        profile_page.wait_for_profile()
        profile_page.click_logout()
        login_page.wait_for_login_form()

        assert login_page.get_current_url() == LOGIN_URL
        assert 'Вход' in login_page.get_title()
