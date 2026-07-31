from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    RECOVERY_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    NEW_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_ICON = (By.CSS_SELECTOR, 'div.input__icon.input__icon-action')
    ACTIVE_PASSWORD_FIELD = (
        By.XPATH,
        "//label[text()='Пароль']/parent::div[contains(@class, 'input_status_active')]",
    )
