from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    RECOVER_PASSWORD_LINK = (By.LINK_TEXT, 'Восстановить пароль')
