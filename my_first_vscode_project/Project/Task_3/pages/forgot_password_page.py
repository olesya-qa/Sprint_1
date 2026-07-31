import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Открыть страницу восстановления пароля')
    def open_page(self, url):
        self.open(url)
        self.find_element(ForgotPasswordPageLocators.RECOVERY_TITLE)

    @allure.step('Дождаться формы восстановления пароля')
    def wait_for_recovery_form(self):
        self.find_element(ForgotPasswordPageLocators.RECOVERY_TITLE)

    @allure.step('Получить заголовок формы восстановления')
    def get_title(self):
        return self.get_text(ForgotPasswordPageLocators.RECOVERY_TITLE)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.type_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Клик по «Восстановить»')
    def click_recover(self):
        self.click(ForgotPasswordPageLocators.RECOVER_BUTTON)
