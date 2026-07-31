import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from urls import FORGOT_PASSWORD_URL, LOGIN_URL, RESET_PASSWORD_URL


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Переход на страницу восстановления пароля')
    def test_navigate_to_password_recovery(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open_page(LOGIN_URL)
        login_page.click_recover_password()
        forgot_password_page.wait_for_recovery_form()

        assert forgot_password_page.get_current_url() == FORGOT_PASSWORD_URL
        assert 'Восстановление пароля' in forgot_password_page.get_title()

    @allure.title('Ввод почты и клик по «Восстановить»')
    def test_enter_email_and_recover(self, driver, new_user):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        email = new_user['user_data']['email']

        forgot_password_page.open_page(FORGOT_PASSWORD_URL)
        forgot_password_page.enter_email(email)
        forgot_password_page.click_recover()
        reset_password_page.wait_for_new_password_form()

        assert reset_password_page.get_current_url() == RESET_PASSWORD_URL
        assert 'Восстановление пароля' in reset_password_page.get_title()

    @allure.title('Кнопка показать/скрыть пароль подсвечивает поле')
    def test_show_password_highlights_field(self, driver, new_user):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        email = new_user['user_data']['email']

        forgot_password_page.open_page(FORGOT_PASSWORD_URL)
        forgot_password_page.enter_email(email)
        forgot_password_page.click_recover()
        reset_password_page.wait_for_new_password_form()
        reset_password_page.click_show_password()

        assert reset_password_page.is_password_field_active()
