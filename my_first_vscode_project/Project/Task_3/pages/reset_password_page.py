import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Дождаться формы ввода нового пароля')
    def wait_for_new_password_form(self):
        self.find_element(ResetPasswordPageLocators.NEW_PASSWORD_INPUT)

    @allure.step('Получить заголовок формы')
    def get_title(self):
        return self.get_text(ResetPasswordPageLocators.RECOVERY_TITLE)

    @allure.step('Клик по иконке показать/скрыть пароль')
    def click_show_password(self):
        self.click(ResetPasswordPageLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверить, что поле пароля подсвечено')
    def is_password_field_active(self):
        self.find_element(ResetPasswordPageLocators.ACTIVE_PASSWORD_FIELD)
        return True
