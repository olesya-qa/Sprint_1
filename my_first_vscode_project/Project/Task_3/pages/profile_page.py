import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Дождаться страницы профиля')
    def wait_for_profile(self):
        self.find_element(ProfilePageLocators.PROFILE_HINT)

    @allure.step('Получить текст подсказки профиля')
    def get_profile_hint(self):
        return self.get_text(ProfilePageLocators.PROFILE_HINT)

    @allure.step('Клик по «История заказов»')
    def click_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Клик по «Выход»')
    def click_logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
