import uuid

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from helpers import create_ad, get_created_ad_on_profile, open_profile_page, register_user
from locators import AdAuthModalLocators, MainPageLocators


class TestCreateAd:

    def test_create_ad_by_unauthorized_user(self, driver):
        wait = WebDriverWait(driver, 15)
        wait.until(
            EC.element_to_be_clickable(MainPageLocators.PLACE_AD_BUTTON)
        ).click()
        modal_title = wait.until(
            EC.visibility_of_element_located(AdAuthModalLocators.MODAL_TITLE)
        )

        assert (
            modal_title.text
            == 'Чтобы разместить объявление, авторизуйтесь'
        )

    def test_create_ad_by_authorized_user(self, driver):
        register_user(driver)
        ad_title = f'Ad_{uuid.uuid4().hex[:6]}'
        create_ad(driver, ad_title, 'Описание товара', '1500')
        open_profile_page(driver)
        created_ad = get_created_ad_on_profile(driver, ad_title)

        assert ad_title in created_ad.text
