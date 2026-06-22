from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import register_user
from locators import MainPageLocators


class TestLogout:

    def test_logout_user(self, driver):
        register_user(driver)

        wait = WebDriverWait(driver, 15)
        wait.until(
            EC.element_to_be_clickable(MainPageLocators.LOGOUT_BUTTON)
        ).click()
        login_button = wait.until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        user_name_elements = driver.find_elements(*MainPageLocators.USER_NAME)
        user_avatar_elements = driver.find_elements(*MainPageLocators.USER_AVATAR)

        assert login_button.is_displayed()
        assert len(user_name_elements) == 0
        assert len(user_avatar_elements) == 0
