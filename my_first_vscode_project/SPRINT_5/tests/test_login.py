from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL, USER_PASSWORD
from helpers import login_user, logout_user, register_user
from locators import MainPageLocators


class TestLogin:

    def test_login_user(self, driver):
        email = register_user(driver)
        logout_user(driver)
        login_user(driver, email, USER_PASSWORD)

        wait = WebDriverWait(driver, 15)
        user_name = wait.until(
            EC.visibility_of_element_located(MainPageLocators.USER_NAME)
        )
        user_avatar = driver.find_element(*MainPageLocators.USER_AVATAR)

        assert driver.current_url == BASE_URL
        assert 'User' in user_name.text
        assert user_avatar.is_displayed()
