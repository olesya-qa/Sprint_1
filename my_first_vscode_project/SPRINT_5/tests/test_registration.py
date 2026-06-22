from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL, USER_PASSWORD
from helpers import (
    fill_registration_form,
    generate_email,
    get_field_error_class,
    go_to_main_page,
    logout_user,
    open_registration_form,
    register_user,
    submit_registration_form,
    wait_for_authorization,
)
from locators import AuthPopupLocators, MainPageLocators, RegistrationFormLocators


class TestRegistration:

    def test_registration_user(self, driver):
        email = generate_email()
        open_registration_form(driver)
        fill_registration_form(driver, email, USER_PASSWORD)
        submit_registration_form(driver)
        wait_for_authorization(driver)
        go_to_main_page(driver)

        wait = WebDriverWait(driver, 15)
        user_name = wait.until(
            EC.visibility_of_element_located(MainPageLocators.USER_NAME)
        )
        user_avatar = driver.find_element(*MainPageLocators.USER_AVATAR)

        assert driver.current_url == BASE_URL
        assert 'User' in user_name.text
        assert user_avatar.is_displayed()

    def test_registration_with_invalid_email(self, driver):
        open_registration_form(driver)
        wait = WebDriverWait(driver, 15)
        wait.until(
            EC.visibility_of_element_located(AuthPopupLocators.EMAIL_INPUT)
        ).send_keys('invalid_email')
        wait.until(
            EC.element_to_be_clickable(AuthPopupLocators.CREATE_ACCOUNT_BUTTON)
        ).click()
        error_message = wait.until(
            EC.visibility_of_element_located(AuthPopupLocators.ERROR_MESSAGE)
        )

        email_error_class = get_field_error_class(
            driver, RegistrationFormLocators.EMAIL_FIELD
        )
        password_error_class = get_field_error_class(
            driver, RegistrationFormLocators.PASSWORD_FIELD
        )
        repeat_password_error_class = get_field_error_class(
            driver, RegistrationFormLocators.REPEAT_PASSWORD_FIELD
        )

        assert error_message.text == 'Ошибка'
        assert 'inputError' in email_error_class
        assert 'inputError' in password_error_class
        assert 'inputError' in repeat_password_error_class

    def test_registration_existing_user(self, driver):
        email = register_user(driver)
        logout_user(driver)
        open_registration_form(driver)
        fill_registration_form(driver, email, USER_PASSWORD)
        submit_registration_form(driver)

        wait = WebDriverWait(driver, 15)
        error_message = wait.until(
            EC.visibility_of_element_located(AuthPopupLocators.ERROR_MESSAGE)
        )
        email_error_class = get_field_error_class(
            driver, RegistrationFormLocators.EMAIL_FIELD
        )
        password_error_class = get_field_error_class(
            driver, RegistrationFormLocators.PASSWORD_FIELD
        )
        repeat_password_error_class = get_field_error_class(
            driver, RegistrationFormLocators.REPEAT_PASSWORD_FIELD
        )

        assert error_message.text == 'Ошибка'
        assert 'inputError' in email_error_class
        assert 'inputError' in password_error_class
        assert 'inputError' in repeat_password_error_class
