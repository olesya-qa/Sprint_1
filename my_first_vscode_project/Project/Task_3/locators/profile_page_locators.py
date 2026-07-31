from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_HINT = (By.XPATH, "//p[contains(@class, 'Account_text')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
