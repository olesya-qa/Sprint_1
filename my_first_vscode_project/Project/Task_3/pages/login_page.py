import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Открыть страницу входа')
    def open_page(self, url):
        self.open(url)
        self.find_element(LoginPageLocators.LOGIN_TITLE)

    @allure.step('Клик по «Восстановить пароль»')
    def click_recover_password(self):
        self.click(LoginPageLocators.RECOVER_PASSWORD_LINK)

    @allure.step('Получить заголовок формы входа')
    def get_title(self):
        return self.get_text(LoginPageLocators.LOGIN_TITLE)

    @allure.step('Дождаться формы входа')
    def wait_for_login_form(self):
        self.find_element(LoginPageLocators.LOGIN_TITLE)
