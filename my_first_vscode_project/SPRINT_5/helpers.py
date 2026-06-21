import uuid

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL, USER_PASSWORD
from locators import (
    AuthPopupLocators,
    CreateAdPageLocators,
    MainPageLocators,
    ProfilePageLocators,
    RegistrationFormLocators,
)


def generate_email():
    return f'user_{uuid.uuid4().hex[:8]}@mail.ru'


def open_registration_form(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    wait.until(
        EC.visibility_of_element_located(AuthPopupLocators.LOGIN_SUBMIT_BUTTON)
    )
    wait.until(
        EC.element_to_be_clickable(AuthPopupLocators.NO_ACCOUNT_BUTTON)
    ).click()
    wait.until(
        EC.visibility_of_element_located(AuthPopupLocators.REPEAT_PASSWORD_INPUT)
    )


def fill_registration_form(driver, email, password):
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.visibility_of_element_located(AuthPopupLocators.EMAIL_INPUT)
    ).send_keys(email)
    driver.find_element(*AuthPopupLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPopupLocators.REPEAT_PASSWORD_INPUT).send_keys(password)


def submit_registration_form(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.element_to_be_clickable(AuthPopupLocators.CREATE_ACCOUNT_BUTTON)
    ).click()


def open_login_form(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)).click()
    wait.until(
        EC.visibility_of_element_located(AuthPopupLocators.LOGIN_SUBMIT_BUTTON)
    )


def fill_login_form(driver, email, password):
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.visibility_of_element_located(AuthPopupLocators.EMAIL_INPUT)
    ).send_keys(email)
    driver.find_element(*AuthPopupLocators.PASSWORD_INPUT).send_keys(password)


def submit_login_form(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.element_to_be_clickable(AuthPopupLocators.LOGIN_SUBMIT_BUTTON)
    ).click()


def wait_for_authorization(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(
        lambda browser: browser.execute_script(
            "return localStorage.getItem('islogin')"
        ) == 'true'
    )


def go_to_main_page(driver):
    wait = WebDriverWait(driver, 15)
    driver.get(BASE_URL)
    wait.until(EC.url_to_be(BASE_URL))


def register_user(driver, email=None, password=USER_PASSWORD):
    user_email = email or generate_email()
    open_registration_form(driver)
    fill_registration_form(driver, user_email, password)
    submit_registration_form(driver)
    wait_for_authorization(driver)
    go_to_main_page(driver)
    return user_email


def login_user(driver, email, password=USER_PASSWORD):
    open_login_form(driver)
    fill_login_form(driver, email, password)
    submit_login_form(driver)
    wait_for_authorization(driver)
    go_to_main_page(driver)


def logout_user(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)
    ).click()
    wait.until(
        EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
    )


def get_field_error_class(driver, field_locator):
    field = driver.find_element(*field_locator)
    parent = field.find_element(By.XPATH, './..')
    return parent.get_attribute('class')


def create_ad(driver, title, description, price):
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)
    ).click()
    wait.until(EC.url_contains('create-lisiting'))
    wait.until(
        EC.visibility_of_element_located(CreateAdPageLocators.TITLE_INPUT)
    ).send_keys(title)
    wait.until(
        EC.element_to_be_clickable(CreateAdPageLocators.DESCRIPTION_INPUT)
    ).send_keys(description)
    driver.find_element(*CreateAdPageLocators.PRICE_INPUT).send_keys(price)

    category = driver.find_element(*CreateAdPageLocators.CATEGORY_INPUT)
    category.find_element(*CreateAdPageLocators.DROPDOWN_ARROW).click()
    wait.until(
        EC.element_to_be_clickable(CreateAdPageLocators.CATEGORY_BOOKS_OPTION)
    ).click()

    city = driver.find_element(*CreateAdPageLocators.CITY_INPUT)
    city.find_element(*CreateAdPageLocators.DROPDOWN_ARROW).click()
    wait.until(
        EC.element_to_be_clickable(CreateAdPageLocators.CITY_MOSCOW_OPTION)
    ).click()

    wait.until(
        EC.element_to_be_clickable(CreateAdPageLocators.CONDITION_NEW_RADIO)
    ).click()
    wait.until(
        EC.element_to_be_clickable(CreateAdPageLocators.PUBLISH_BUTTON)
    ).click()
    wait.until(EC.url_to_be(BASE_URL))


def open_profile_page(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.element_to_be_clickable(MainPageLocators.USER_AVATAR)
    ).click()
    wait.until(EC.url_contains('profile'))
    wait.until(
        EC.visibility_of_element_located(ProfilePageLocators.MY_ADS_SECTION)
    )


def get_created_ad_on_profile(driver, title):
    wait = WebDriverWait(driver, 15)
    return wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, f"//*[contains(text(),'{title}')]")
        )
    )
