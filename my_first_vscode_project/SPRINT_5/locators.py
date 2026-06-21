from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
    PLACE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выйти')]")
    USER_NAME = (By.CSS_SELECTOR, 'h3.profileText.name')
    USER_AVATAR = (By.CSS_SELECTOR, 'button.circleSmall')


class AuthPopupLocators:
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Пароль']")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Повторите пароль']")
    ERROR_MESSAGE = (By.XPATH, "//*[text()='Ошибка']")


class RegistrationFormLocators:
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    REPEAT_PASSWORD_FIELD = (By.NAME, 'submitPassword')


class CreateAdPageLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Название']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Стоимость']")
    CATEGORY_INPUT = (By.NAME, 'category')
    CITY_INPUT = (By.NAME, 'city')
    CATEGORY_BOOKS_OPTION = (By.XPATH, "//span[text()='Книги']")
    CITY_MOSCOW_OPTION = (By.XPATH, "//span[text()='Москва']")
    DROPDOWN_ARROW = (By.XPATH, './ancestor::div[contains(@class,"dropDownMenu")][1]//button')
    CONDITION_NEW_RADIO = (
        By.XPATH,
        "//div[contains(@class,'radioUnput_shell')]//label[text()='Новый']",
    )
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(),'Опубликовать')]")


class AdAuthModalLocators:
    MODAL_TITLE = (
        By.XPATH,
        "//*[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]",
    )


class ProfilePageLocators:
    MY_ADS_SECTION = (By.XPATH, "//*[contains(text(),'Мои объявления')]")
